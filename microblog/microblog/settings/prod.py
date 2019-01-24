from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# DBの設定
DATABASES = {
    'default': {
    }
}

INSTALLED_APPS += (
    'gunicorn',
)