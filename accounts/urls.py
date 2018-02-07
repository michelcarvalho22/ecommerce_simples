# coding=utf-8

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    url('registro/', views.register, name='register')
]
