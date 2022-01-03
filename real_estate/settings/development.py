from .baseSettings import *




DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE'),
        'NAME': env('POSTGRES_NAME'),
        'USER':env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT')
    }
}

STATIC_URL = '/staticfiles/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
   
    BASE_DIR / 'frontend/build/staticfiles'
]
MEDIA_ROOT = BASE_DIR / 'images'
STATIC_ROOT = BASE_DIR / 'staticfiles'
