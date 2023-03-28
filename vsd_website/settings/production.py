import os
from vsd_website.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["verisdev.au", "www.verisdev.au", "web-production-71b7.up.railway.app"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

UPLOAD_ROOT = "media/uploads/"

DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"
