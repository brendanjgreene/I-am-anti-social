from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config(
    "mysql://b303b6a76a6c1a:a0cce2e7@eu-cdbr-west-01.cleardb.com/heroku_42692666c95cfac?reconnect=true")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_DN78rrac6Vda1ito3iAlshPc')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_6VOZz0QegToWvMWYrcGF5qFs')

# Paypal environment variables
SITE_URL = 'https://i-am-anti-social.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://i-am-anti-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'brendanjgreene-merchant2@gmail.com'
