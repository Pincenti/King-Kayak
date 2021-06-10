from flask import render_template, redirect, url_for
from .import bp as shop
import stripe
from app.stripe import stripe_data
from .models import Product, Cart, Order

stripe.api_key = stripe_data.get('secret_key')

@shop.route('/')
def index():
    context = {
        'products': stripe.Product.list(limit=3)
    }
    return render_template('shop.html', **context)