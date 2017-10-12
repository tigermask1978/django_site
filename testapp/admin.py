# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person, Musician, Album, Teacher, Course

# Register your models here.
admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Teacher)
admin.site.register(Course)
