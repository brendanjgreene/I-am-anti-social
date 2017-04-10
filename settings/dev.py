from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE_SECRET key>')

# Paypal environment variables
# SITE_URL = 'http://127.0.0.1:8000'
# PAYPAL_NOTIFY_URL = '<your ngrok URL>'
# PAYPAL_RECEIVER_EMAIL = '<your Paypal merchant email>'
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'brendanjgreene-merchant2@gmail.com'

# Stripe environment variables
# STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_DN78rrac6Vda1ito3iAlshPc')
# STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_6VOZz0QegToWvMWYrcGF5qFs')

# Paypal environment variables
# SITE_URL = 'http://127.0.0.1:8000'
# PAYPAL_NOTIFY_URL = 'http://a62a95fe.ngrok.io/a-very-hard-to-guess-url/'
# PAYPAL_RECEIVER_EMAIL = 'brendanjgreene-merchant2@gmail.com'
