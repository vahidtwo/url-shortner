import os
import sys
from pathlib import Path

import pymysql
import urllib3
from decouple import config

# TODO get all credentials and secrets from vault
urllib3.disable_warnings()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config("SECRET_KEY", "")

DEBUG = config("DEBUG", False, cast=bool)
PHASE = config("PHASE", default="local")

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_extensions",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "shortener",
]

APPEND_SLASH = False

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "settings.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("MYSQL_DATABASE"),
        "USER": config("MYSQL_USER"),
        "PASSWORD": config("MYSQL_PASSWORD"),
        "HOST": config("DB_HOST", "localhost"),
        "PORT": config("DB_PORT", "3306"),
        "OPTIONS": {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            "charset": "utf8mb4",
        },
        # Tell Django to build the test database with the 'utf8mb4' character set
        "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_unicode_ci", "CONN_MAX_AGE": None},
    }
}

CORS_ALLOW_ALL_ORIGINS = True  # todo: change this


REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Patch pymysql instead of mysqlclient
pymysql.version_info = (1, 4, 6, "final", 0)
pymysql.install_as_MySQLdb()

SPECTACULAR_SETTINGS = {
    "SERVE_INCLUDE_SCHEMA": True,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "SERVE_PUBLIC": False,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],  # TODO revise it
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "auth.User"

REDIS_URI = config("PERSIST_REDIS_URI", "redis://127.0.0.1:9685/")

# for exposing metrics
STATSD_HOST = config("STATSD_HOST", "localhost")
STATSD_PORT = config("STATSD_PORT", "8125")
STATSD_PREFIX = config("STATSD_PREFIX", "enigma")
STATSD_DEBUG = True


REDIS_PORT = config("REDIS_PORT", "6379")
REDIS_HOST = config("REDIS_HOST", "localhost")
REDIS_PASSWORD = config("REDIS_PASSWORD", "")
