import os
from vsd_website.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_URL = "static/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

UPLOAD_ROOT = "media/uploads/"

DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"
