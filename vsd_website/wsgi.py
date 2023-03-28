"""
WSGI config for vsdwebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if bool(os.environ.get("VSD_DEBUG").strip()):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vsd_website.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vsd_website.settings.production")

application = get_wsgi_application()
