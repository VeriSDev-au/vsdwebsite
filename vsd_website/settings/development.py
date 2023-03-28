import os
from vsd_website.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

STATIC_ROOT = "static/static/"
STATIC_URL = "/static/static/"

MEDIA_ROOT = "static/media"
MEDIA_URL = "/static/media/"

UPLOAD_ROOT = "uploads/"

DOWNLOAD_URL = "/static/media/downloads"
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
