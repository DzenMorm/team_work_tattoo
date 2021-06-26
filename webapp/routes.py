from webapp import app
from webapp.forms import LoginForm, RegistrationForm
from flask import render_template


@app.route('/')
def index():
    title = 'Начальная страница'
    nav_bar = 'Вход'
    reg = 'Регистрация'
    return render_template('index.html', page_title=title,
                           nav_bar_link=nav_bar, reg=reg)


@app.route('/login')
def login():
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@app.route('/registration')
def registration():
    title = 'Регистрация'
    login_form = RegistrationForm()
    return render_template('registration.html', page_title=title,
                           form=login_form)

