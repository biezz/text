# coding:utf-8

from django.conf.urls import url
from .views import article_list, create_article
from .views import article_detail


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list, name='article_list'),
    url(r'^create/(?P<block_id>\d+)', create_article, name='create_article'),
    url(r'^detail/(?P<article_id>\d+)/$', article_detail, name="article_detail"),
    ]
