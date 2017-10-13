# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import PageInfo
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    limit = 10
    page_info = PageInfo.objects
    paginator = Paginator(page_info, limit)
    page = request.GET.get('page',1)
    loaded = paginator.page(page)
    context = {
       'PageInfo': loaded
    }
    return render(request, 'ganji/index.html', context)