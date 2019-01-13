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

from photo_album_server import settings
from photo_album_server.api_urls.version1 import router_v1
from user.views import AuthTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_v1.urls)),  # 相应的接口

    path('api-token-auth/', AuthTokenView.as_view()),  # token 认证

    re_path('static/(?P<path>.*)$', static.serve,
            {'document_root': settings.STATIC_ROOT}, name='static'),
]
