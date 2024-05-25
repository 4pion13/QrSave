# -*- coding: utf-8 -*-
import os
from .base import *

ALLOWED_HOSTS = ['qrsave-test.novikov-sa.ru', 'localhost', '192.168.68.67']
CSRF_TRUSTED_ORIGINS = ['https://qrsave-test.novikov-sa.ru']
CORS_ORIGIN_WHITELIST = ['https://qrsave-test.novikov-sa.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'qrsave',
        'HOST': os.getenv('DB_HOST'),
        'PORT': 5432,
        'USER': 'qrsave',
        'PASSWORD': 'Qwerty123',
    }
}

STATIC_ROOT = '/var/www/qrsave/static'
MEDIA_ROOT = '/var/www/qrsave/media'