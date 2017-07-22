# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Post(models.Model):
    title_text = models.CharField(max_length=20)
    body_text = models.TextField
    publish_date = models.DateTimeField('data published')

    def __str__(self):
        return str(self.title_text)+str(self.body_text)+str(self.publish_date)

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)
