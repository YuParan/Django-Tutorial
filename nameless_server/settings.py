"""
Django settings for nameless_server project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import yaml
from pathlib import Path

from nameless_server import logger_config

from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

with open(f'{BASE_DIR}/system/environments.yaml', 'r') as f:
    ENVIRONMENT = yaml.load(f, Loader=yaml.FullLoader)

with open(f'{BASE_DIR}/system/keys.yaml', 'r') as f:
    KEYS = yaml.load(f, Loader=yaml.FullLoader)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = KEYS['secure_settings']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = KEYS['secure_settings']['allowed_hosts']


# CORS Settings
# https://github.com/adamchainz/django-cors-headers

CORS_ORIGIN_ALLOW_ALL = True  # If 'DEBUG = False', It should be False in production
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = tuple(KEYS['secure_settings']['cors_exceptions'])
CORS_ALLOW_HEADERS = tuple(
    list(default_headers) +
    KEYS['secure_settings']['cors_allow_headers']
)
CSRF_TRUSTED_ORIGINS = KEYS['secure_settings']['csrf_trusted_origins']


# django-rest-framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',

    # custom applications
    # Not yet
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    # custom middlewares
    # Not yet
]

ROOT_URLCONF = 'nameless_server.urls'


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


# WSGI & ASGI application settings
WSGI_APPLICATION = 'nameless_server.wsgi.application'
ASGI_APPLICATION = 'nameless_server.asgi.application'


# Database - Not Used yet
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = ENVIRONMENT['settings']['language']
TIME_ZONE = ENVIRONMENT['settings']['timezone']

USE_I18N = True
USE_L10N = True

# setting local time
USE_TZ = True


# Logger setting
LOGGING = logger_config.get_logging_config(
    project_name=ENVIRONMENT['server']['name'],
    log_dir=(BASE_DIR / ENVIRONMENT['settings']['log_dir'])
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = ENVIRONMENT['settings']['static_url']
STATIC_ROOT = ENVIRONMENT['settings']['static_root']

# Media files
MEDIA_URL = ENVIRONMENT['settings']['media_url']
MEDIA_ROOT = ENVIRONMENT['settings']['media_root']

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
