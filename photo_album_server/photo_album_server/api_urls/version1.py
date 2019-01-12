# -*- coding: utf-8 -*-
"""
这个是这个项目的第一个版本的 api url 文件
"""
from rest_framework import routers

from photos.views import PhotoViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'photos', PhotoViewSet)
