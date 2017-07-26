# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Post

from django.template import loader


from django.http import Http404

def homepage(request):
    latest_post_list = Post.objects.order_by('-publish_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'kitty/homepage.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def post(request, url_text):
    post = get_object_or_404(Post, pk=url_text)
    return render(request, "kitty/post.html", {'post': post})
    # try:
    #     post = Post.objects.get(pk=url_text)
    # except Post.DoesNotExist:
    #     raise Http404("没有这篇博文的哦")
    #
    # return render(request, "kitty/post.html", {'post': post})

def about(request):
    return HttpResponse("about me")

def contact(request):
    return HttpResponse("contact me")

# Create your views here.
