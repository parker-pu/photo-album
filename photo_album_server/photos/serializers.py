# Create your views here.
from rest_framework import serializers

from photos.models import PhotoModel, PhotoCacheModel


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """用户的配置信息
    """

    class Meta:
        model = PhotoModel
        fields = "__all__"


class PhotoCacheSerializer(serializers.HyperlinkedModelSerializer):
    """用户的配置信息
    """

    class Meta:
        model = PhotoCacheModel
        fields = (
            'id', 'name', 'describe', 'photo_url',
            'thumbnail', 'insert_time', 'update_time'
        )
