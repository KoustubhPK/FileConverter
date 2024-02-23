"""
Django settings for FormatGo project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import datetime
from pathlib import Path
from config import SECRET_KEY, EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pdfgo.apps.PdfgoConfig',
    'ckeditor',       # Install ckeditor,
    'bleach'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pdfgo.middleware.AlreadyLoggedMiddleware',
]

ROOT_URLCONF = 'FormatGo.urls'
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

AWS_QUERYSTRING_AUTH = False

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
    "default": {
        "removePlugins": "stylesheetparser",
    }

}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
WSGI_APPLICATION = 'FormatGo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email Validation

EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST  # Replace with your SMTP server host
EMAIL_PORT = EMAIL_PORT  # Replace with the SMTP server port (587 is a common port for TLS)
EMAIL_USE_TLS = EMAIL_USE_TLS  # Use TLS (True for port 587, False for port 465)
EMAIL_HOST_USER = EMAIL_HOST_USER  # Replace with your email address
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD  # Replace with your email password

#Logged user prevention
LOGIN_REDIRECT_URL = '/'
#LOGIN_URL = 'login'

#Password Reset
PASSWORD_RESET_TIMEOUT = 3600  # Set the password reset link validity time (in seconds)
PASSWORD_RESET_TIMEOUT = 1800
PASSWORD_RESET_CONFIRM_URL = 'reset/{uidb64}/{token}/'  # Set the password reset confirmation URL pattern

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
TIME_ZONE = 'Asia/Kolkata'  # Replace 'Asia/Kolkata' with your desired timezone


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



MEDIA_URL = '/media/'   
STATIC_URL = '/staticfiles/'
DATA_UPLOAD_MAX_NUMBER_FILES = 10240