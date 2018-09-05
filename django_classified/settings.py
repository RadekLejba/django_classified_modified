import os

from django.conf import settings
from django_classified import get_version

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'vp)gy*xy*ezf*9efo#1t3zao%ecyp4jz94sk)gb_g@hk%!r^y2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrapform',
    'sorl.thumbnail',
    'django_classified',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_classified.urls'

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
                'django_classified.context_processors.common_values',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_classified.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THUMBNAIL_CACHE_TIMEOUT = 3600 * 24 * 365
THUMBNAIL_DEBUG = True
THUMBNAIL_PREFIX = 'cache/'


"""
Default settings for Django Classified app.
"""

# Site currency
CURRENCY = getattr(settings, 'DCF_CURRENCY', 'USD')

# Display credits in footer
DISPLAY_CREDITS = getattr(settings, 'DCF_DISPLAY_CREDITS', True)

# Max items per page
ITEM_PER_PAGE = getattr(settings, 'DCF_ITEM_PER_PAGE', 10)

# Max items per user
ITEM_PER_USER_LIMIT = getattr(settings, 'DCF_ITEM_PER_USER_LIMIT', 20)

# Hide contact details for unauthorized users
LOGIN_TO_CONTACT = getattr(settings, 'DCF_LOGIN_TO_CONTACT', True)

# Max related items displayed on page
RELATED_LIMIT = getattr(settings, 'DCF_RELATED_LIMIT', 6)

# Max items included to the RSS feed
RSS_LIMIT = getattr(settings, 'DCF_RSS_LIMIT', 100)

# Site default description
SITE_DESCRIPTION = getattr(settings, 'DCF_SITE_DESCRIPTION', 'Classified Advertisements Powered by Django')

# Default site name
SITE_NAME = getattr(settings, 'DCF_SITE_NAME', 'Django Classified Ads')

# Default site id
SITE_ID = 1

# Sitemap items limit
SITEMAP_LIMIT = getattr(settings, 'DCF_SITEMAP_LIMIT', 1000)

# Display empty group in the groups list
DISPLAY_EMPTY_GROUPS = getattr(settings, 'DCF_DISPLAY_EMPTY_GROUPS', False)

VERSION = get_version()

# Email backend setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
