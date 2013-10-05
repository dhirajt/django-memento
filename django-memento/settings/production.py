from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dhiraj Thakur', 'dhirajthakur92@facebook.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-memento',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}