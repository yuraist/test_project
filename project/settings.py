# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys


PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(PROJECT_PATH, 'apps'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sht8!0^#fn9!y9x&sh34_wgoo&b^%qoq+bz3=vkr!#m_gsm_q%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'pipeline',
    
    'base',
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

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


PIPELINE_STYLESHEETS = {
    'libs': {
        'source_filenames': (
            'css/bootstrap.css',
            'css/bootstrap-theme.css',
        ),
        'output_filename': 'compressed/css/libs.css',
    },
    'base': {
        'source_filenames': (
            'base/css/layout.css',
        ),
        'output_filename': 'compressed/css/base.css',
    },
}


PIPELINE_JAVASCRIPT = {
    'libs': {
        'source_filenames': (
            'js/jquery-2.2.4.js',
            'js/lodash-3.10.1.js',
            'js/bootstrap.js',
            'js/backbone.js',
            'js/backbone.marionette.v2.4.7.js',
        ),
        'output_filename': 'compressed/js/libs.js',
    },
    'tasks': {
        'source_filenames': (
            'base/js/app.js',
            'base/js/models.js',
            'base/js/TaskView.js',
            'base/js/TasksListView.js',
        ),
        'output_filename': 'compressed/js/tasks.js',
    }
}


PIPELINE = {
    # PIPELINE_ENABLED should always be `not DEBUG` as:
    # - PipelineFinder works only when PIPELINE_ENABLED = False
    # - static file serve works only when DEBUG = True
    'PIPELINE_ENABLED': not DEBUG,

    # only work when `PIPELINE_ENABLED` is False
    # in most cases that means "dev mode", so disable collector by default
    'PIPELINE_COLLECTOR_ENABLED': False,

    'DISABLE_WRAPPER': True,

    # uncomment this, if you need less
    # 'COMPILERS': (
    #     'pipeline.compilers.less.LessCompiler',
    # ),
    # 'LESS_BINARY': 'lessc',
    # 'LESS_ARGUMENTS': '',

    'STYLESHEETS': PIPELINE_STYLESHEETS,
    'JAVASCRIPT': PIPELINE_JAVASCRIPT,

    'SHOW_ERRORS_INLINE': False,
}


STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticroot')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'


LOGIN_URL = '/admin/login/'
