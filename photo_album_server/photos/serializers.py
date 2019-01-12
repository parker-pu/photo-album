# Create your views here.
from rest_framework import serializers

from photos.models import PhotoModel


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """用户的配置信息
    """

    class Meta:
        model = PhotoModel
        fields = "__all__"

    def update(self, instance, validated_data):
        print(validated_data)
        pass

    def create(self, validated_data):
        print(validated_data)
        # instance = self.Meta.model.objects.create(**validated_data)
        # return instance
