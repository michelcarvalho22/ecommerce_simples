
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from hello import views

urlpatterns = [

    url('^$', views.index, name='index'),
    url('^contato/$', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]
