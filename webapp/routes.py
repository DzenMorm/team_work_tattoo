import os
from webapp import app
from webapp.forms import LoginForm, RegistrationForm, MasterForm, ImageForm
from flask import render_template, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from flask_login import current_user, login_user, logout_user
from webapp.models import db, Auth, City, Master, Image


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
            return redirect(url_for('profile_master'))
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
        db.session.add(new_register)
        db.session.commit()
        login_user(new_register)

        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('register_master'))
    flash('Пожалуйста, исправьте ошибки в форме регистрации')
    return redirect(url_for('register'))


@app.route('/register-master')
def register_master():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    title = 'Регистрация тату-мастера'
    form = MasterForm()
    return render_template('register_master.html', page_title=title,
                           form=form)


@app.route('/process-reg-master', methods=['POST'])
def process_reg_master():
    form = MasterForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = [{
                'name': form.city.data
            }]
            db.session.bulk_insert_mappings(City, city, return_defaults=True)
            city_id = city[0]['id']
        else:
            city_id = city.id

        master = Master(
            name=form.name.data,
            last_name=form.last_name.data,
            address=form.address.data,
            number_phone=form.number_phone.data,
            email=form.email.data,
            city_id=city_id,
            auth_id=current_user.id)

        db.session.add(master)
        db.session.commit()
        return redirect(url_for('profile_master'))
    return redirect(url_for('process_reg_master'))


@app.route('/profile-master')
def profile_master():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Профиль'
    form = ImageForm()
    images = Image.query.filter(Image.master_id == current_user.master.id).all()
    return render_template('profile_master.html', title=title, form=form, images=images)


@app.route('/save-image', methods=['POST'])
def save_image():
    form = ImageForm()
    if form.validate_on_submit():
        for image in form.image.data:
            filename = secure_filename(image.filename)
            path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            image_for_db = Image(
                name=filename,
                path=path,
                master_id=current_user.master.id
            )
            db.session.add(image_for_db)
            db.session.commit()
        return redirect('profile-master')
