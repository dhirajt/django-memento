from .base import *


ADMINS = (
    ('Dhiraj Thakur', 'dhirajthakur92@facebook.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'memento',
        'USER': 'root',
        'PASSWORD': 'sql123',
        'HOST': '',
        'PORT': '',
    }
}



# You might want to use sqlite3 for testing in local as it's much faster.
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'memento',
            'USER': 'root',
            'PASSWORD': 'sql123',
            'HOST': '',
            'PORT': '',
        }
    }