from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.galeria',
    'apps.usuarios',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👍 Necessário para o Render servir estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# AWS S3 — 
# -------------------------------------------------------------------

AWS_ACCESS_KEY_ID = str(os.getenv('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = str(os.getenv('AWS_SECRET_ACCESS_KEY'))
AWS_STORAGE_BUCKET_NAME = str(os.getenv('AWS_STORAGE_BUCKET_NAME'))
AWS_S3_REGION_NAME = 'us-east-1'  # 👈 Mantido fixo, como você pediu
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False

# -------------------------------------------------------------------
# STATIC + MEDIA — MANTENDO SEU PADRÃO DE ARQUITETURA ORIGINAL
# -------------------------------------------------------------------

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {"location": "media"},
    },
    "staticfiles": {
        # Você estava usando S3 para static — mantendo!
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {"location": "static"},
    },
}

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'setup/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # corrigido p/ Render

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success'
}
