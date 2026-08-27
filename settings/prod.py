
from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
DEBUG = env.bool('DEBUG', default=True)
SECRET_KEY = env("SECRET_KEY")
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


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

SECURE_HSTS_SECONDS = env('SECURE_HSTS_SECONDS')
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False)
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=False)
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)
