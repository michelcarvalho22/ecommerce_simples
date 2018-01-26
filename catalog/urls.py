# coding=utf-8
from django.conf.urls import url
from django.urls import path

import catalog.views
from . import views

app_name = 'catalog'

urlpatterns = [
   path('', catalog.views.product_list, name='product_list'),
   url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
   url(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]
