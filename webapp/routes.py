from webapp import app
from webapp.forms import LoginForm, RegistrationForm, MasterForm, SalonForm, UserForm, ImageForm
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from webapp.models import db, Auth, City, Master, User, Salon, Image
from werkzeug.utils import secure_filename
import os


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
        db.session.add(new_register)
        db.session.commit()
        # user = Auth.query.filter(Auth.email == form.email.data).first()
        login_user(new_register)
        flash('Вы успешно зарегистрировались!')
        if form.role.data == '1':
            return redirect(url_for('user_reg'))
        elif form.role.data == '2':
            return redirect(url_for('master_reg'))
        elif form.role.data == '3':
            return redirect(url_for('salon_reg'))
        return redirect(url_for('login'))
    flash('Пожалуйста, исправьте ошибки в форме регистрации')
    return redirect(url_for('register'))


@app.route('/salon-reg')
def salon_reg():
    form = SalonForm()
    title = 'Регистрация Салона'
    return render_template('salonreg.html', page_title=title,
                           form=form)


@app.route('/process-salon-reg', methods=['POST'])
def process_salon_reg():
    form = SalonForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = City(name=form.city.data)
            print(city)
            db.session.add(city)
            db.session.commit()

        new_salon = Salon(
            name=form.name.data,
            number_phone=form.number_phone.data,
            address=form.address.data,
            email=form.email.data,
            city_id=city.id,
            auth_id=current_user.id)

        print(new_salon)

        db.session.add(new_salon)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/user-reg')
def user_reg():
    form = UserForm()
    title = 'Регистрация пользователя'
    return render_template('userreg.html', page_title=title,
                           form=form)


@app.route('/process-user-reg', methods=['POST'])
def process_user_reg():
    form = UserForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = City(name=form.city.data)
            print(city)
            db.session.add(city)
            db.session.commit()

        new_user = User(
            name=form.name.data,
            last_name=form.last_name.data,
            number_phone=form.number_phone.data,
            email=form.email.data,
            date_of_birth=form.date_of_birth.data,
            city_id=city.id,
            auth_id=current_user.id)

        print(new_user)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/master-reg')
def master_reg():
    title = 'Регистрация тату-мастера'
    form = MasterForm()
    return render_template('masterreg.html', page_title=title,
                           form=form)


@app.route('/process-master-reg', methods=['POST'])
def process_master_reg():
    form = MasterForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = City(name=form.city.data)
            print(city)
            db.session.add(city)
            db.session.commit()

        salon = Salon.query.filter(Salon.name == form.salon.data).first()
        if not salon:
            master = Master(
                name=form.name.data,
                last_name=form.last_name.data,
                number_phone=form.number_phone.data,
                address=form.address.data,
                email=form.email.data,
                city_id=city.id,
                auth_id=current_user.id)
        else:
            master = Master(
                name=form.name.data,
                last_name=form.last_name.data,
                number_phone=form.number_phone.data,
                address=form.address.data,
                email=form.email.data,
                salon_id=salon.id,
                city_id=city.id,
                auth_id=current_user.id)

        db.session.add(master)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/profile-master')
def profile_master():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Профиль'
    form = ImageForm()
    images = Image.query.filter(Image.master_id == current_user.master.id).all()
    print(images)
    return render_template('profile_master.html', title=title, form=form, images=images)


@app.route('/save-image', methods=['POST'])
def save_image():
    form = ImageForm()
    if form.validate_on_submit():
        for image in form.image.data:
            filename = secure_filename(image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            image_for_db = Image(
                name=filename,
                path=path,
                master_id=current_user.master.id
            )
            db.session.add(image_for_db)
            db.session.commit()
        return redirect('profile-master')
