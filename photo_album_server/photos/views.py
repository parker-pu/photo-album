# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from custom.permission import CustomPermission
from photos.models import PhotoModel
from photos.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    # class PhotoView(APIView):
    """ 处理图片
    """
    permission_classes = (CustomPermission,)  # 设置权限

    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer

    # @staticmethod
    # def post(request, *args, **kwargs):
    #     """ 重写 create 这个方法
    #
    #     把图片处理成缩略图，同时把图片存储到本地
    #     :return:
    #     """
    # print(request)
    # data = request.data
    # data["thumbnail"] = ''
    # serializer = self.get_serializer(data=data)
    # serializer.is_valid(raise_exception=True)
    # self.perform_create(serializer)
    # headers = self.get_success_headers(serializer.data)
    # return Response(
    #     serializer.data,
    #     status=status.HTTP_201_CREATED,
    #     headers=headers
    # )
    # return Response('ok')
