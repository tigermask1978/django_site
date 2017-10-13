# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *  #MongoDB的Django插件，实现ORM
# from mongoengine import connect
# connect('XiaoZhu', host='127.0.0.1', port=27017)

#ORM
class PageInfo(Document):
    price = FloatField()
    address = StringField()

    meta = {
        'collection': 'page_info'
    }

# for i in PageInfo.objects:
#     print i.price, i.address
