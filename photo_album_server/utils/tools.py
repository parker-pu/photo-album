#!/usr/share/app/anaconda3/bin/python3
# encoding: utf-8  

""" 
@version: v1.0 
@author: pu_yongjun
@license: Apache Licence
"""

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def img_to_square(im_pic):
    """ 把图片处理成正方形
    :param im_pic:
    :return:
    """
    w, h = im_pic.size
    if w >= h:
        w_start = (w - h) * 0.618
        box = (w_start, 0, w_start + h, h)
        region = im_pic.crop(box)
    else:
        h_start = (h - w) * 0.618
        box = (0, h_start, w, h_start + w)
        region = im_pic.crop(box)
    return region


def to_thumbnail(img_obj):
    """ 这个函数的作用是把图片处理成缩略图
    :param img_obj:
    :return:
    """
    pic = Image.open(img_obj)
    region = img_to_square(pic)

    # 先保存到磁盘io
    pic_io = BytesIO()
    region.save(pic_io, pic.format)

    # 再转化为InMemoryUploadedFile数据
    pic_file = InMemoryUploadedFile(
        file=pic_io,
        field_name=None,
        name=img_obj.name,
        content_type=img_obj.content_type,
        size=pic.size,
        charset=None
    )
    return pic_file
