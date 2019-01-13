# Create your views here.
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from custom.auth_token import (
    ExpiringTokenAuthentication
)
from custom.permission import CustomPermission
from photos.models import PhotoModel
from photos.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """ 处理图片
    """
    permission_classes = (CustomPermission,)  # 设置权限
    parser_classes = (MultiPartParser,)

    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer

    @staticmethod
    def img_to_square(im_pic):
        """ 把图片处理成正方形
        :param im_pic:
        :return:
        """
        w, h = im_pic.size
        if w >= h:
            w_start = (w - h) * 0.618
            box = (w_start, 0, w_start + h, h)
            region = im_pic.crop(box)
        else:
            h_start = (h - w) * 0.618
            box = (0, h_start, w, h_start + w)
            region = im_pic.crop(box)
        return region

    def to_thumbnail(self, img_obj):
        """ 这个函数的作用是把图片处理成缩略图
        :param img_obj:
        :return:
        """
        pic = Image.open(img_obj)
        region = self.img_to_square(pic)

        # 先保存到磁盘io
        pic_io = BytesIO()
        region.save(pic_io, pic.format)

        # 再转化为InMemoryUploadedFile数据
        pic_file = InMemoryUploadedFile(
            file=pic_io,
            field_name=None,
            name=img_obj.name,
            content_type=img_obj.content_type,
            size=pic.size,
            charset=None
        )
        return pic_file

    def create(self, request, *args, **kwargs):
        """ 新增文件
        """
        img_obj = request.FILES.get('photo')
        if not img_obj:
            return Response(status=203, data={"message": "上传文件错误"})

        # 图片处理成缩略图
        # thumbnail = self.to_thumbnail(img_obj)

        # 认证请求信息,获取用户与token信息
        user, token = ExpiringTokenAuthentication().authenticate(request)

        back_data = PhotoModel.objects.create(
            user=user,
            name=img_obj.name,
            describe=request.data.get('describe'),
            thumbnail=img_obj
        )
        return Response(
            data={
                "id": back_data.id,
                "name": back_data.name
            },
            status=status.HTTP_201_CREATED,
        )
