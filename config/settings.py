"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ff%*l=oqh@r-&x8rc#89jitb^$(dvf0h1j1f5ze@tzyobq=9ts'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
'0.0.0.0'
]


# Application definition

INSTALLED_APPS = [
    'social_django',
    'accounts',
    'shop',
    'cart',
    'orders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'cart.context_processors.cart',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
  'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
  'social_core.backends.google.GoogleOpenId',  # for Google authentication
  'social_core.backends.google.GoogleOAuth2',  # for Google authentication
  'social_core.backends.github.GithubOAuth2',
  'social_core.backends.twitter.TwitterOAuth',
  'social_core.backends.facebook.FacebookOAuth2',

  'django.contrib.auth.backends.ModelBackend',
  'social_core.backends.instagram.InstagramOAuth2',
)

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'products/')

CART_SESSION_ID = 'cart'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'shop:product_list'


# github keys
SOCIAL_AUTH_GITHUB_KEY = 'b17986d65f772cfa5204'
SOCIAL_AUTH_GITHUB_SECRET = 'c0787d07512319859b0b8c7b5286b05ac0d2e44e'

# facebook keys
SOCIAL_AUTH_FACEBOOK_KEY = '314700825747438'
SOCIAL_AUTH_FACEBOOK_SECRET = '670de008bb0f537f268fc1bc12394bcc'

# google+ keys
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '127248638826-hiku5idecj4buhqtepqvlanum3n1g3eu.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XQ_FJOlPqNRrsrDjrO_ZSHdr'

# intagram keys
SOCIAL_AUTH_INSTAGRAM_KEY = '9e89b37078fa4000a8c0ae76c3f4fd86'
SOCIAL_AUTH_INSTAGRAM_SECRET = 'd47776a5f42d4caeb59b7fbdd1dd2e13'

