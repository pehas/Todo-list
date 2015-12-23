"""
Django settings for apps project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__) + '/../')

#LOGIN AND
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mhgyj+q+bnq%x8-+c8et$s87mvl=90hh705r_afs$=1$8_9t*$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'accounts.User'


AUTHENTICATION_BACKENDS = [
    'apps.accounts.auth.EmailOrUsernameModelBackend'
]

PROXY = True
PROXY_HOST = 'localhost:8000'
PROXY_TYPE = 'http'
PROXY_AUTH = 'express:page'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
	'django.contrib.humanize',

	'django_crontab',

    'apps.todo',
	'apps.diesel',
	'apps.accounts',
	'apps.finance',
)

CRONJOBS = [
	('*/1 * * * *', 'apps.diesel.management.commands.up.up_user'),
	('*/1 * * * *', 'apps.cron.up_user')
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'apps.finance.context_processors.categories',
)

SITE_ID = 1

ROOT_URLCONF = 'apps.urls'

SGI_APPLICATION = 'apps.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR + '/templates/',
)



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR +  '/static/'
MEDIA_URL =  '/media/'
MEDIA_ROOT = PROJECT_DIR + '/media/'
