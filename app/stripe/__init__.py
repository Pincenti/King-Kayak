import stripe
from flask import current_app as app

stripe_data = {
    'publishable_key': app.config.get('STRIPE_PUBLISHABLE_KEY'),
    'secret_key': app.config.get('STRIPE_SECRET_KEY')
}
