from flask import Flask, render_template
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Начальная страница'
        nav_bar = 'Вход'
        reg = 'Регистрация'
        return render_template('index.html', page_title=title, nav_bar_link=nav_bar, reg=reg)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app