"""
Setting detail for development environment

Static files need in the development environment can be stored
in the same server with the application 
"""

import os
from vsd_website.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]

MEDIA_ROOT = "staticfiles/media"
MEDIA_URL = "/staticfiles/media/"

UPLOAD_ROOT = "uploads/"

DOWNLOAD_URL = "/staticfiles/media/downloads"
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
