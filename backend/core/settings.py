"""
Django settings for hando project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t9r^l0@)bk3#ezvsl6@jw9k$d0m41%nu9j)b7nuq@prq=+x4+f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app', 'hando-backend-production.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://hando-backend-production.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'knox',
    'drf_spectacular',
    'django_extensions',
    'storages',
    
    'app.users',
    'app.lookups',
    'app.services',
    'app.cart',
    'app.orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'users.User'

# Setup Localization

from django.utils.translation import gettext as _
import os

# Available Languages
LANGUAGES = [
    ('en', ('English')),
    ('ar', ('Arabic')) 
]
# Locales available path

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/'),
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': ['knox.auth.TokenAuthentication', 'rest_framework.authentication.TokenAuthentication'],
}

# DRF Spectacular (Swagger) Settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Hando API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SERVE_AUTHENTICATION' : ['rest_framework.authentication.TokenAuthentication',],
    'SCHEMA_PATH_PREFIX': '/api',
}

from datetime import timedelta

REST_KNOX = {
    'TOKEN_TTL' : timedelta(days=90)
}

# Static files (CSS, JavaScript, Images) , Media Files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
MEDIA_URLS ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Digital Ocean Storage Settings
# STORAGES = {
#     "staticfiles": {
#         # use default storage
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": {
#             "bucket_name": config('DIGITAL_OCEAN_BUCKET'),
#             "endpoint_url": config('DIGITAL_OCEAN_BUCKET_ENDPOINT'),
#             "access_key": config('DIGITAL_OCEAN_ACCESS_KEY'),
#             "secret_key": config('DIGITAL_OCEAN_SECRET_KEY'),
#             "region_name": config('DIGITAL_OCEAN_REGION_NAME'),
#             "location": "static",
#             "default_acl": "",
#         },
#     },
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": {
#             "bucket_name": config('DIGITAL_OCEAN_BUCKET'),
#             "endpoint_url": config('DIGITAL_OCEAN_BUCKET_ENDPOINT'),
#             "access_key": config('DIGITAL_OCEAN_ACCESS_KEY'),
#             "secret_key": config('DIGITAL_OCEAN_SECRET_KEY'),
#             "region_name": config('DIGITAL_OCEAN_REGION_NAME'),
#             "location": "media",
#             "default_acl": "",
#         },
#     },
# }

# print('STORAGES', STORAGES)


AWS_ACCESS_KEY_ID = config('CLOUD_STORAGE_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = config('CLOUD_STORAGE_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = config('CLOUD_STORAGE_BUCKET')
AWS_S3_ENDPOINT_URL = config('CLOUD_STORAGE_BUCKET_ENDPOINT')
AWS_S3_REGION_NAME = config('CLOUD_STORAGE_REGION_NAME')
AWS_S3_SIGNATURE_VERSION = config('CLOUD_STORAGE_SIGNATURE_VERSION')
AWS_QUERYSTRING_EXPIRE = 86400


# AWS_DEFAULT_ACL = None
# AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'mysite/static'),
# ]
# STATIC_URL = 'https://%s/' % (AWS_S3_ENDPOINT_URL)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# media
# AWS_LOCATION = 'media'
# MEDIA_URL = 'https://%s/' % (AWS_S3_ENDPOINT_URL)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
