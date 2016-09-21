import os

from leanwebsite import settings


DATABASES={
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    }
}

