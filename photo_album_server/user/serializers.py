# Create your views here.
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户的配置信息
    """

    class Meta:
        model = User
        fields = "__all__"
