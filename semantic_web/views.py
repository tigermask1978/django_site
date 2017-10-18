# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'semantic_web/index_data.html')


def chart(request):
    return render(request, 'semantic_web/chart2.html')

