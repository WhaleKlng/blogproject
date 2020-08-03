from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogproject',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        # 'PASSWORD': 'zhuyaxin'
        'PASSWORD': 'OFFERshow@520'
    }
}
