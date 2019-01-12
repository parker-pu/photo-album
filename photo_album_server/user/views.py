# Create your views here.
import datetime

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


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
        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'token_expires': token.created + datetime.timedelta(hours=24 * 14),
            'user_name': user.username
        })
