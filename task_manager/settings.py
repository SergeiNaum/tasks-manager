"""
Django settings for task_manager project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["webserver", "127.0.0.1", "77.222.53.154"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "manager.apps.ManagerConfig",
    "users.apps.UsersConfig",
    "statuses.apps.StatusesConfig",
    "tasks.apps.TasksConfig",
    "labels.apps.LabelsConfig",

    "django_bootstrap5",
    "django_filters",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
]

ROOT_URLCONF = "task_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "task_manager.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

LANGUAGES = [
    ("en", "English"),
    ("ru", "Russian"),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'console': {
#             'format': '%(name)-12s %(levelname)-8s %(message)s'
#         },
#         'json_formatter': {
#             '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
#             'format': '%(asctime)s %(name)s %(levelname)s %(message)s',
#         },
#
#         'file': {
#             'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
#
#         },
#         'verbose': {
#             'format': '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
#         },
#
#     },
#     'handlers': {
#         'console': {
#             'class': 'rich.logging.RichHandler',
#             'formatter': 'console',
#             'level': 'INFO',
#         },
#         'file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'formatter': 'json_formatter',
#             'filename': 'logs/debug.json'
#         },
#         'mail_admins': {
#             'level': 'WARNING',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'rotating_file': {  # Создаем rotating file
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/debug.json',
#             'maxBytes': 1024 * 1024 * 200,  # 10 Мб
#             'backupCount': 5,  # Количество файлов ротации
#             'encoding': 'utf-8'
#             # 'formatter': 'json_formatter',
#             # 'level': 'DEBUG',
#
#         },
#     },
#     'loggers': {
#         '': {
#             'level': 'INFO',
#             'handlers': ['console'],
#             'propagate': True
#         },
#         'django.request': {
#             'level': 'WARNING',
#             'handlers': ['file', 'mail_admins', 'rotating_file'],
#             'propagate': True
#         },
#         'django.db.backends': {
#             'level': 'WARNING',
#             'handlers': ['file', 'mail_admins', 'rotating_file'],
#             'propagate': True
#         },
#         'django.db.security': {
#             'level': 'WARNING',
#             'handlers': ['file', 'mail_admins', 'rotating_file'],
#             'propagate': True
#         }
#     }
# }

ROLLBAR = {
    "access_token": "891568aa386f432ca550af5eb3920f2a",
    "environment": "development" if DEBUG else "production",
    "code_version": "1.0",
    "root": BASE_DIR,
}
