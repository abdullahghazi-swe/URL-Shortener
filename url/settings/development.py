from .base import *

SECRET_KEY = 'django-insecure-8x8c44scpdn=+()9@@cwg0no@cc%n6q)ahj=tki6l13&p(8!h#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}