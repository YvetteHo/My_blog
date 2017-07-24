# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

def homepage(request):
    latest_post_list = Post.objects.order_by('-publish_date')[:5]
    output = ', '.join([p.title_text for p in latest_post_list])
    return HttpResponse(output)

def post(request):
    return HttpResponse("Post")

def about(request):
    return HttpResponse("about me")

def contact(request):
    return HttpResponse("contact me")



# Create your views here.
