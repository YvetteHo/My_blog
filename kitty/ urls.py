from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage")
    url(r'^(about)/$', views.about, name="about")
    url(r'^(contact)/$', views.contact, name="contact")
    url(r'^[\s\S]/$', views.post, name="post")
]
