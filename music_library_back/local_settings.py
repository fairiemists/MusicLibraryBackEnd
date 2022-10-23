
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-))3q&m=_5w84dj664q55t6)$s0cbu=pkr3yj9^)c0va!a$7$h='

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_back_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}

