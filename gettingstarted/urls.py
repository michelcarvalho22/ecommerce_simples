from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

import hello.views

urlpatterns = [

    url(r'^$', hello.views.index, name='index'),
    url(r'^contato/$', hello.views.contatos, name='contatos'),
    url(r'^produto/$', hello.views.produto, name='produto'),
    url(r'^produtos/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]
