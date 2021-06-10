# from flask.helpers import flash
# from werkzeug.utils import redirect
# # from app import app
# from flask import render_template
# from flask import request
# from flask import url_for, current_app as app
# from flask import flash
# from app.blueprints.authentication.models import User
# from flask_login import login_user, logout_user, current_user

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/shop')
# def shop():
#     return render_template('shop.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user = User.query.filter_by(email=request.form.get('email')).first()
#         if user is None or not user.check_password(request.form.get('password')):
#             flash('Either that user does not exist or the password is incorrect.')
#             return redirect(url_for('login'))
#         remember_me = True if request.form.get('checked') is not None else False
#         login_user(user, remember=remember_me)
#         flash('You have successfully logged in!')
#         return redirect(url_for('home'))
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         u = User()
#         u.from_dict(request.form)
#         u.save()
#         return redirect(url_for('login'))
#     return render_template('register.html')