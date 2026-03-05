"""
Django settings for core project.
"""
from dotenv import load_dotenv
load_dotenv()
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Update: Using environment variable to clear W009
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-$w@af*dkx@ba59h*n)92bru(uwkmr7*__1t%#p*d7gwej7tww3')

# SECURITY WARNING: don't run with debug turned on in production!
# Update: Using environment variable to clear W018
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Update: Added local and placeholder domain to clear W020
# Added www.explore.ugc.edu.gh to the list
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.explore.ugc.edu.gh', '.herokuapp.com', '.railway.app']


# Application definition

INSTALLED_APPS = [
    'programs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Added for production static file handling
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
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # Added to handle images in templates
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Added for deployment

# --- MEDIA FILE CONFIGURATION ---
# This is where Django will store your uploaded program images
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/6.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Updated to ensure the project looks in your static folder for the brochure
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "images",
]

# --- AUTHENTICATION REDIRECTS ---

LOGIN_URL = 'login' 

# Where the user goes after logging in
LOGIN_REDIRECT_URL = 'staff_dashboard'

# Where the user goes after logging out
LOGOUT_REDIRECT_URL = 'login'

# --- PRODUCTION SECURITY SETTINGS ---
# Clears W004, W008, W012, W016 when DEBUG is False
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # Trust the educational domain for form submissions
    CSRF_TRUSTED_ORIGINS = ['https://www.explore.ugc.edu.gh']
