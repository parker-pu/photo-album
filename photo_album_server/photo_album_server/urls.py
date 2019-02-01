"""photo_album_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

from photo_album_server import settings
from user.views import AuthTokenView, UserViewSet
from rest_framework import routers
from photos.views import PhotoViewSet, PhotoCacheViewSet, OriginalPhotoViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'photos-cache', PhotoCacheViewSet)
router_v1.register(r'photos', PhotoViewSet)
router_v1.register(r'users', UserViewSet)

API_TITLE = '相册'
API_DESCRIPTION = '这是个人用来玩的相册'

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_v1.urls)),  # 相应的接口

    # 获取原始图片
    path('api/v1/original-photos', OriginalPhotoViewSet.as_view()),

    # 相应的API文档
    path('docs/', include_docs_urls(
        title=API_TITLE,
        description=API_DESCRIPTION,
        authentication_classes=[],
        permission_classes=[]
    )),

    path('api-token-auth/', AuthTokenView.as_view()),  # token 认证

    re_path('static/(?P<path>.*)$', static.serve,
            {'document_root': settings.STATIC_ROOT}, name='static'),
]
