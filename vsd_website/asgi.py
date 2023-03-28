"""
ASGI config for vsdwebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if bool(os.environ.get("VSD_DEBUG")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vsd_website.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vsd_website.settings.production")

application = get_asgi_application()
