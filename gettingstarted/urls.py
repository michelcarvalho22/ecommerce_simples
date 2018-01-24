
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

import hello.views


urlpatterns = [

    url(r'^$', hello.views.index, name='index'),
    url(r'^contato/$', hello.views.contatos, name='contatos'),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]
