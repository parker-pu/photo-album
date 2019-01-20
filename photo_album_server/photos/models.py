from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PhotoModel(models.Model):
    """ 图片存储
    """
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE,
        default='',
        verbose_name='用户'
    )
    name = models.TextField(verbose_name="图片名称")
    describe = models.TextField(verbose_name="图片描述")
    photo_url = models.TextField(verbose_name="图片的路径")
    thumbnail = models.ImageField(
        verbose_name="缩略图"
        , upload_to="static/user_img"
    )
    insert_time = models.DateTimeField(auto_now=True, verbose_name="插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'photo'  # 数据库源配置


class PhotoCacheModel(models.Model):
    """ 图片缓存存储
    """
    user = models.ForeignKey(
        User,
        related_name='cuser',
        on_delete=models.CASCADE,
        default='',
        verbose_name='用户'
    )
    name = models.TextField(verbose_name="图片名称")
    describe = models.TextField(verbose_name="图片描述")
    photo_url = models.TextField(verbose_name="图片的路径")
    thumbnail = models.ImageField(
        verbose_name="缩略图"
        , upload_to="static/data/images/cache"
    )
    insert_time = models.DateTimeField(auto_now=True, verbose_name="插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'photo_cache'  # 数据库源配置
