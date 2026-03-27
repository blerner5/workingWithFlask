from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from . import auth
from .forms import LoginForm, RegistrationForm
from .models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login(): if


current_user.is_authenticated:
return redirect(url_for('task.index'))
form = LoginForm()
if form.validate_on_submit(): user = User.query.filter_by(email=form.email.data).first()
if user is None or not user.check_password(form.password.data): flash('Invalid email or password')
return redirect(url_for('auth.login'))
login_user(user, remember=form.remember_me.data)
next_page = request.args.get('next')
if not next_page or url_parse(next_page).netloc != '': next_page = url_for('task.index')
return redirect(next_page)
return render_template('auth/login.html', form=form) @ auth.route('/logout')


def logout(): logout_user()


return redirect(url_for('task.index')) @ auth.route('/register', methods=['GET', 'POST'])


def register(): if


current_user.is_authenticated:
return redirect(url_for('task.index'))
form = RegistrationForm()
if form.validate_on_submit(): user = User(username=form.username.data, email=form.email.data)
user.set_password(form.password.data)
db.session.add(user)
db.session.commit()
flash('Registration successful! You can now log in.')
return redirect(url_for('auth.login'))
return render_template('auth/register.html', form=form)
