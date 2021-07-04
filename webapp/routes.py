from webapp import app
from webapp.forms import LoginForm, RegistrationForm, SalonForm, UserForm
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from webapp.models import db, Auth


@app.route('/')
def index():
    title = 'Начальная страница'
    nav_bar = 'Вход'
    reg = 'Регистрация'
    return render_template('index.html', page_title=title,
                           nav_bar_link=nav_bar, reg=reg)


@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@app.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Auth.query.filter(Auth.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('Вы успешно вошли на сайт')
            login_user(user)
            return redirect(url_for('index'))
    flash('Неправильная почта или пароль')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))


@app.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Регистрация'
    login_form = RegistrationForm()
    return render_template('registration.html', page_title=title,
                           form=login_form)


@app.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_register = Auth(email=form.email.data)
        new_register.set_password(form.password.data)
        if form.role.data == '1':
            return redirect(url_for('user_reg'))
        elif form.role.data == '2':
            pass
        elif form.role.data == '3':
            return redirect(url_for('salon_reg'))
        db.session.add(new_register)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('login'))
    flash('Пожалуйста, исправьте ошибки в форме регистрации')
    return redirect(url_for('register'))


@app.route('/salon-reg')
def salon_reg():
    form = SalonForm()
    title = 'Регистрация Салона'
    return render_template('salon.html', page_title=title,
                           form=form)


@app.route('/user-reg')
def user_reg():
    form = UserForm()
    title = 'Регистрация пользователя'
    return render_template('user.html', page_title=title,
                           form=form)
