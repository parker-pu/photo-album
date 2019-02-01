# Create your views here.
import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from custom.permission import CustomPermission
from user.serializers import UserSerializer


class AuthTokenView(ObtainAuthToken):
    """ 这个类的作用是提供自定义的 Toke
    """

    def post(self, request, *args, **kwargs):
        """ POST 方法返回 Token
        """
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # 先删除 Token，再生产一个
        # Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'token_expires': token.created + datetime.timedelta(hours=24 * 14),
            'user_name': user.username
        })


class UserViewSet(viewsets.ModelViewSet):
    """ 处理用户
    """
    permission_classes = (CustomPermission,)  # 设置权限

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def filter_get_fields(data):
        """ 过滤查询字段
        """
        fields = ["id", "username", "email", "is_staff"]

        for line in data:
            line["id"] = str(line["url"]).split('/')[-2]
            new_line = list(map(lambda x: line.get(x), fields))
            yield dict(zip(fields, new_line))

    def list(self, request, *args, **kwargs):
        """ 这个函数的作用是用来查看数据
        """
        back_data = {
            "id": request.user.id,
            "last_login": request.user.last_login,
            "is_superuser": request.user.is_superuser,
            "username": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "is_staff": request.user.is_staff,
            "is_active": request.user.is_active,
            "date_joined": request.user.date_joined
        }
        return Response(back_data)

    def create(self, request, *args, **kwargs):
        """ 重写 create 这个方法
        :return:
        """
        data = request.data
        data["password"] = make_password(data.get("password"))
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """ 更改用户信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.data.get('password'):
            request.data["password"] = make_password(request.data.get('password'))

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
