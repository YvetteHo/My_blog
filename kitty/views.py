# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response

from django.http import HttpResponse, Http404

from .models import Post, About

from django.template import loader

from django.shortcuts import render_to_response

from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

def homepage(request):
    post_list = Post.objects.order_by('-publish_date')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.numpages)

    return render(request, 'kitty/homepage.html', {'posts': posts})
    # after_range_num = 5
    # before_range_num = 4
    # try:
    #     page=int(request.GET.get('page', '1'))
    #     if page < 1:
    #         page=1
    # except ValueError:
    #     page=1
    # post_list = Post.objects.order_by('-publish_date')
    # paginator = Paginator(post_list, 10)
    # try:
    #     post_list = paginator.page(page)
    # except (EmptyPage, InvalidPage, PageNotAnInteger):
    #     post_list = paginator.page(1)
    # if page > after_range_num:
    #     page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    # else:
    #     page_range = paginator.page_range[0:int(page)+before_range_num]
    # return render_to_response('kitty/homepage.html', {'post_list': post_list})
    #

    # time = 0
    # post_list = Post.objects.order_by('-publish_date')[:(time+5)]
    # context = {'post_list': post_list}
    # return render(request, 'kitty/homepage.html', context)

def post(request, url_text):
    post = get_object_or_404(Post, pk=url_text)
    return render(request, "kitty/post.html", {'post': post})

def about(request):
    try:
        self_intro_text = About.objects.get(pk=1)
    except About.DoesNotExist:
        self_intro_text = 'Nothing'
    return render(request, 'kitty/about.html', {'self_intro_text': self_intro_text})


# Create your views here.
