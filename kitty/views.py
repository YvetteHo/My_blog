# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Post, About

from django.template import loader


from django.http import Http404

def homepage(request):
    latest_post_list = Post.objects.order_by('-publish_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'kitty/homepage.html', context)

def post(request, url_text):
    post = get_object_or_404(Post, pk=url_text)
    return render(request, "kitty/post.html", {'post': post})

def about(request):
    try:
        self_intro_text = About.objects.all().first()
    except About.DoesNotExist:
        self_intro_text = 'Nothing'
    return render(request, 'kitty/about.html', {'self_intro_text': self_intro_text})

def contact(request):
    return HttpResponse("contact me")

# Create your views here.
