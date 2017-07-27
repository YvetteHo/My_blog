# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, About

admin.site.register(Post)
admin.site.register(About)
# Register your models here.
