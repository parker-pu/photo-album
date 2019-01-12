# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomPermission(BasePermission):
    """ 这个函数是自定义权限的函数
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            pass
        return request.user and request.user.is_authenticated
