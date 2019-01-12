from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PhotoModel(models.Model):
    """ 源数据库配置
    """
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE,
        default='',
        verbose_name='用户'
    )
    describe = models.TextField(verbose_name="图片描述")
    # thumbnail = models.TextField(verbose_name="缩略图")
    thumbnail = models.ImageField(verbose_name="缩略图")
    insert_time = models.DateTimeField(auto_now=True, verbose_name="插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'photo'  # 数据库源配置
