
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
        'DISABLE_SERVER_SIDE_CURSORS': True
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

SECURE_HSTS_SECONDS = env('SECURE_HSTS_SECONDS')
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False)
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=False)
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# For serving static files directly from S3
# AWS_S3_URL_PROTOCOL = 'https'
AWS_S3_USE_SSL = env('AWS_S3_USE_SSL')
AWS_S3_VERIFY = env('AWS_S3_VERIFY')

AWS_S3_FILE_OVERWRITE = env('AWS_S3_FILE_OVERWRITE')

AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)

STORAGES = {
    "default": {
        "BACKEND": "trootech_project.storages.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "trootech_project.storages.StaticStorage",
    },
}

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

AWS_DEFAULT_ACL = env('AWS_DEFAULT_ACL')
