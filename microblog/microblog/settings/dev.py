from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DBの設定
DATABASES = {
    'default': {
        # DB名
        'ENGINE': 'django.db.backends.sqlite3',
        # DBファイルの保存名
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
