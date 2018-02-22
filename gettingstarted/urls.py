from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings

from django.views.static import serve as serve_static
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

from hello import views

urlpatterns = [

    url('^$', views.index, name='index'),
    url('^contato/$', views.contact, name='contact'),
    url('^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url('^sair/$', logout, {'next_page': 'index'}, name='logout'),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('compras/', include('checkout.urls', namespace='checkout')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


admin.site.site_header = 'UsePointMix'
