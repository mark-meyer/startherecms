from __future__ import absolute_import, unicode_literals

from .base import *
import dj_database_url
import os

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = False

SECURE_SSL_REDIRECT = True
PREPEND_WWW = True
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware', # must be there in middlewares
 )

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

#Creates a separate search index from local
#ALGOLIA['INDEX_PREFIX'] = 'prod'

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
