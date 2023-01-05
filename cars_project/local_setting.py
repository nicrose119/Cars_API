# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+-v6j&jmkqk+e+xnw3wg24+!q$0=4lovzhn&fbn)ex^ftir2de'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password1'
    }
}
