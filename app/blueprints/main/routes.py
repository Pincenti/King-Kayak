from flask.helpers import flash
from werkzeug.utils import redirect
# from app import app
from flask import render_template
from flask import request
from flask import url_for
from flask import flash
from app.blueprints.authentication.models import User
from flask_login import login_user, logout_user, current_user
from app.blueprints.main import bp as main

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/shop')
def shop():
    return render_template('shop.html')
