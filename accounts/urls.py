# coding=utf-8

from django.conf.urls import url
from . import views


app_name = 'accounts'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^alterar-dados/$', views.update_user, name='update_user'),
    url('^alterar-senha/$', views.update_password, name='update_password'),
    url('^registro/$', views.register, name='register'),
]
