"""
Django settings for task_manager project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG_ENV = os.getenv('DEBUG')
DEBUG = DEBUG_ENV if DEBUG_ENV else True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task_manager',
    'task_manager.task',
    'django_bootstrap5',
    'task_manager.mark',
    'task_manager.users',
    'task_manager.status',
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


ROOT_URLCONF = 'task_manager.urls'

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

WSGI_APPLICATION = 'task_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


BOOTSTRAP5 = {
    # The complete URL to the Bootstrap CSS file
    "css_url": {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
        "integrity": "sha384-Ky/zIbSAUnTOrdrDgQ8X5ujPkvRV+NlOTu8hC26i9dZIUl3Y6PnRYCin1/Nab2jK",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-yQe6O3xh6S1CWS/PbXlWe+oj/09cS2+ZjZOr+AL5Xo8g+Fd6EE6EJQ+JdAldjKlI",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS theme file (None means no theme)
    "theme_url": None,

    # The URL to the Popper.js JavaScript file
    "popper_url": {
        "url": "https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.10.2/umd/popper.min.js",
        "integrity": "sha384-dLntqEDY/PqotUnLswM63LjVfBhFJ04dQm9Bqt6Q31LGhiDZ4T+jxIt1GtyadF0a",
        "crossorigin": "anonymous",
    },

    # The URL to the jQuery JavaScript file (full)
    "jquery_url": {
        "url": "https://code.jquery.com/jquery-3.6.4.min.js",
        "integrity": "sha384-o9p3AWiZ6FqE2Ie0I2r6PivL5o2I1h3hGZHa5CqVVe6cu4YLQFqygm9sz4Mzmocn",
        "crossorigin": "anonymous",
    },

    # The URL to the jQuery JavaScript file (slim)
    "jquery_slim_url": {
        "url": "https://code.jquery.com/jquery-3.6.4.slim.min.js",
        "integrity": "sha384-mtXp8FmtZ6J3pDBM8a1S7yt3JP9a3pc5u2eRV2APeaqU6ooj9w8U7o3U3w3qRFHp",
        "crossorigin": "anonymous",
    },

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap4.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript False|falsy|slim|full (default=False)
    # False - means tag bootstrap_javascript use default value - `falsy` and does not include jQuery)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': 'required',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'is-invalid',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'is-valid',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers': {
        'default': 'bootstrap5.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap5.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap5.renderers.FieldRenderer',
        'inline': 'bootstrap5.renderers.InlineFieldRenderer',
    },
}

