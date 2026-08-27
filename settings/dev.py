
from .base import *
import environ


env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool('DEBUG', default=True)
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),      # Must be created in PostgreSQL first
        'USER': env('DB_USER'),      # Database user role
        'PASSWORD': env('DB_PASSWORD'), # User's password
        'HOST': env('DB_HOST'),               # 'localhost' or remote database IP
        'PORT': env('DB_PORT'),                    # Default PostgreSQL port
    }
}
