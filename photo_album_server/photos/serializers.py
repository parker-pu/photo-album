# Create your views here.
from rest_framework import serializers

from photos.models import PhotoModel


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """用户的配置信息
    """

    class Meta:
        model = PhotoModel
        fields = "__all__"
