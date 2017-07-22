# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length=20)
    body_text = models.TextField
    publish_date = models.DateTimeField('data published')