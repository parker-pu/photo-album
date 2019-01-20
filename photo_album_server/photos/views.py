# Create your views here.
import os
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from custom.permission import CustomPermission
from photos.models import PhotoModel, PhotoCacheModel
from photos.serializers import PhotoSerializer, PhotoCacheSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile


class PhotoViewSet(viewsets.ModelViewSet):
    """ 处理图片
    """
    permission_classes = (CustomPermission,)  # 设置权限

    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer

    def perform_destroy(self, instance):
        """ 删除图片
        """
        instance.thumbnail.delete()
        instance.delete()

    def get_queryset(self):
        """ 筛选出数据库中只有当前用户的数据
        """
        user = self.request.user
        return PhotoModel.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        """ 处理缓存文件

        作用主要是把缓冲的图片移动到相应的数据库中
        """

        # 获取用户的信息
        user = self.request.user

        # 从缓冲区中取出数据放入到对应的数据库中
        # 更新描述信息
        try:
            PhotoCacheModel.objects.filter(user=user) \
                .update(describe=request.data.get('describe'))

            # 把缓冲区中的数据移动到对应的数据中
            cache_img_data = PhotoCacheModel.objects.filter(user=user)
            for line_data in cache_img_data:
                PhotoModel.objects.create(
                    user=line_data.user,
                    describe=line_data.describe,
                    name=line_data.name,
                    photo_url=line_data.photo_url,
                    thumbnail=line_data.thumbnail,
                    insert_time=line_data.insert_time,
                    update_time=line_data.update_time
                )
                # os.remove(line_data.thumbnail)

            # 删除缓冲区中的数据
            PhotoCacheModel.objects.filter(user=user).delete()

            return Response(
                data="提交成功",
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            print(e)


class PhotoCacheViewSet(viewsets.ModelViewSet):
    """ 处理缓存的图片

    图片上传之后，先缓存一下，等待提交，当用户点击提交之后，就把图片提交
    """
    permission_classes = (CustomPermission,)  # 设置权限
    parser_classes = (MultiPartParser,)

    queryset = PhotoCacheModel.objects.all()
    serializer_class = PhotoCacheSerializer

    def perform_destroy(self, instance):
        """ 删除图片
        """
        instance.thumbnail.delete()
        instance.delete()

    def get_queryset(self):
        """ 筛选出数据库中只有当前用户的数据
        """
        user = self.request.user
        return PhotoCacheModel.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        """ 新增文件
        """
        img_obj = request.FILES.get('photo')
        if not img_obj:
            return Response(status=203, data={"message": "上传文件错误"})

        # 图片处理成缩略图
        # thumbnail = self.to_thumbnail(img_obj)

        # 获取用户信息
        user = self.request.user

        back_data = PhotoCacheModel.objects.create(
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
