# -*- coding: utf-8 -*-
import os

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('db.sql'),
    }
}

TIME_ZONE = 'Asia/Yekaterinburg'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
MEDIA_ROOT = rel('media')

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
LOGIN_URL = '/enter/'
LOGIN_REDIRECT_URL  = '/'

# Make this unique, and don't share it with anybody.
YT_DEVKEY = 'AI39si4IHt6F6YS671on1wtociYyirG3Ys-IMpHhKqf_OqDrwHDFO751yTwAKBb14Bra7emz5jkkOc3tjM8KM-zRP7wEscg3ug'
SECRET_KEY = '7jgijn%yvna&imys$j@8t4o!(+%smkixbl5$^45ds4k&mr(l^c'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'YTupload.urls'

TEMPLATE_DIRS = (
    rel('templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'control',
)

# YTupload settings
ENCODE_DIR_FROM = rel('encode_from')
ENCODE_DIR_TO = rel('encode_to')
YT_LOGIN = ''
YT_PASSWORD = ''
FFMPEG_AR = '22050' # ffmpeg audio sampling frequency => http://www.ffmpeg.org/ffmpeg.html#TOC9
FFMPEG_VB = '1500kbits/s' # ffmpeg video bitrate => http://www.ffmpeg.org/ffmpeg.html#TOC7

try:
    from local_settings import *
except ImportError:
    pass
