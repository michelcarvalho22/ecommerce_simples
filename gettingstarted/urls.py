<<<<<<< HEAD
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
=======
from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
>>>>>>> 9a41ac0e2988172bbf5e17295857bc863053ce8a

from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

<<<<<<< HEAD
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
=======
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
>>>>>>> 9a41ac0e2988172bbf5e17295857bc863053ce8a
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


admin.site.site_header = 'UsePointMix'
