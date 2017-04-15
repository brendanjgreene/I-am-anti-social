from base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# postgres://ogxqyjvfcruvlf:935178df517a3499031327afe7677f5699e2f7b447f8c6a35ab7b498a7febbb3@ec2-79-125-105-164.eu-west-1.compute.amazonaws.com:5432/dbiq93nvlrhcrk

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_DN78rrac6Vda1ito3iAlshPc')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_6VOZz0QegToWvMWYrcGF5qFs')

# Paypal environment variables
SITE_URL = 'https://i-am-anti-social.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://i-am-anti-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'brendanjgreene-merchant2@gmail.com'
