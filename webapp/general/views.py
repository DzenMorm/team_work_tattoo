import os

from webapp.general.forms import LoginForm, RegistrationForm, ImageForm, SearchCityForm

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import current_user, login_user, logout_user
from webapp.db import db

from webapp.general.models import Auth, City, Image

from werkzeug.utils import secure_filename

blueprint = Blueprint('general', __name__, url_prefix='/general')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    title = 'Начальная страница'
    form = SearchCityForm()
    masters = None
    salons = None
    if request.method == 'POST' and form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if city:
            masters = city.masters
            salons = city.salons
        else:
            flash('По данному городу нет информации')
    return render_template('index.html', page_title=title,
                           form=form,
                           masters=masters, salons=salons)


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('general.index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('login/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Auth.query.filter(Auth.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('Вы успешно вошли на сайт')
            login_user(user)
            if current_user.salon:
                return redirect(url_for('salon.profile_salon'))
            elif current_user.master:
                return redirect(url_for('master.profile_master'))
            else:
                return redirect(url_for('general.index'))
    flash('Неправильная почта или пароль')
    return redirect(url_for('general.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('general.index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('general.index'))
    title = 'Регистрация'
    login_form = RegistrationForm()
    return render_template('login/registration.html', page_title=title,
                           form=login_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_register = Auth(email=form.email.data)
        new_register.set_password(form.password.data)
        db.session.add(new_register)
        db.session.commit()
        login_user(new_register)
        flash('Вы успешно зарегистрировались!')
        if form.role.data == '1':
            return redirect(url_for('user.user_reg'))
        elif form.role.data == '2':
            return redirect(url_for('master.master_reg'))
        elif form.role.data == '3':
            return redirect(url_for('salon.salon_reg'))
        return redirect(url_for('general.login'))
    flash('Пожалуйста, исправьте ошибки в форме регистрации')
    return redirect(url_for('general.register'))


@blueprint.route('/save-image', methods=['POST'])
def save_image():
    form = ImageForm()
    if form.validate_on_submit():
        for image in form.image.data:
            filename = secure_filename(image.filename)
            path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            if current_user.master:
                image_for_db = Image(
                    name=filename,
                    path=path,
                    master_id=current_user.master.id
                )
            elif current_user.salon:
                image_for_db = Image(
                    name=filename,
                    path=path,
                    salon_id=current_user.salon.id
                )
            db.session.add(image_for_db)
            db.session.commit()
        if current_user.master:
            return redirect(url_for('master.profile_master'))
        elif current_user.salon:
            return redirect(url_for('salon.profile_salon'))