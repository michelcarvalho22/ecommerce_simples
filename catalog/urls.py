# coding=utf-8


from django.conf.urls import url

from catalog import views


urlpatterns = [
    url(r'^$', views.produtos_list, name='produtos_list'),
]
