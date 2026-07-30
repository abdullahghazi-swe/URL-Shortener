from .base import *
from decouple import config

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="*"
    ).split(",")



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}