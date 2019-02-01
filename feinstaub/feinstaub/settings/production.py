#
# TODOs
#
# rename this file to production.py
#
import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# add your host here:
ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'static'

# Extra places for collectstatic to find static files.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

USE_X_FORWARDED_HOST = True

# set a new secret key:
SECRET_KEY = os.getenv("API_SECRET_KEY", "FIXME")

# set some secrets for APIs
FORECAST_IO_KEY = os.getenv("API_FORECAST_IO_KEY", "FIXME")
