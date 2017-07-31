# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# @python_2_unicode_compatible
# class About(models.Model):
#     self_intro_text = models.TextField(None)
#
#     def __str__(self):
#         return str(self.self_intro_text)

# @python_2_unicode_compatible
class About(models.Model):
    self_intro_text = RichTextUploadingField()
    # def __str__(self):
    #     return ('%s' % self.self_intro_text).encode('utf-8', errors='replace')
    #
    def __str__(self):
        return self.self_intro_text
    # def __unicode__(self):
    #     return self.self_intro_text

# @python_2_unicode_compatible
class Post(models.Model):
    title_text = models.CharField(max_length=20)
    subtitle_text = models.CharField(max_length=20)
    body_text = RichTextUploadingField()
    publish_date = models.DateTimeField('data published')
    url_text = models.CharField(max_length=20, primary_key=True)
    def __unicode__(self):
        return (u'%s') % self.title_text
    # def __str__(self):
    #     return str(self.title_text)+str(self.subtitle_text)+str(self.publish_date)

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)
