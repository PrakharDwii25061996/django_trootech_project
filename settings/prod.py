
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

SECURE_SSL_REDIRECT = env.bool(
    "SECURE_SSL_REDIRECT",
    default=False
)

SESSION_COOKIE_SECURE = env.bool(
    "SESSION_COOKIE_SECURE",
    default=False
)

CSRF_COOKIE_SECURE = env.bool(
    "CSRF_COOKIE_SECURE",
    default=False
)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
