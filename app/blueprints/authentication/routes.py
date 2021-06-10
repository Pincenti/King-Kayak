from flask_login import login_user, logout_user
from flask import redirect, url_for, render_template, request, flash
from app.blueprints.authentication.models import User
from .import bp as auth



@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is None or not user.check_password(request.form.get('password')):
            flash('Either that user does not exist or the password is incorrect.')
            return redirect(url_for('auth.login'))
        remember_me = True if request.form.get('checked') is not None else False
        login_user(user, remember=remember_me)
        flash('You have successfully logged in!')
        return redirect(url_for('main.home'))
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User()
        u.from_dict(request.form)
        u.save()
        return redirect(url_for('auth.login'))
    return render_template('register.html')