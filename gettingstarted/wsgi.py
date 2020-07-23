<<<<<<< HEAD

import os
=======
"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
>>>>>>> 9a41ac0e2988172bbf5e17295857bc863053ce8a

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

application = get_wsgi_application()
