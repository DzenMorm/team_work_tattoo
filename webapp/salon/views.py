from webapp.salon.forms import SalonForm
from webapp.general.forms import ImageForm

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from webapp.db import db

from webapp.general.models import City
from webapp.salon.models import Salon

blueprint = Blueprint('salon', __name__, url_prefix='/salons')


@blueprint.route('/salon-reg')
def salon_reg():
    form = SalonForm()
    title = 'Регистрация Салона'
    if current_user.user:
        return redirect(url_for('general.index'))
    elif current_user.master:
        return redirect(url_for('master.profile_master'))
    elif current_user.salon:
        return redirect(url_for('salon.profile_salon'))
    return render_template('login/salonreg.html', page_title=title,
                           form=form)


@blueprint.route('/process-salon-reg', methods=['POST'])
def process_salon_reg():
    form = SalonForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = City(name=form.city.data)
            db.session.add(city)
            db.session.commit()

        new_salon = Salon(
            name=form.name.data,
            number_phone=form.number_phone.data,
            address=form.address.data,
            email=form.email.data,
            city_id=city.id,
            auth_id=current_user.id)

        db.session.add(new_salon)
        db.session.commit()
        return redirect(url_for('salon.profile_salon'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле "{getattr(form, field).label.text}": {error}')
        return redirect(url_for('general.salon_reg'))


@blueprint.route('/profile-salon')
def profile_salon():
    if not current_user.is_authenticated:
        return redirect(url_for('general.index'))
    title = 'Профиль'
    form = ImageForm()
    images = current_user.salon.images
    return render_template('salon/profile_salon.html', title=title, form=form, images=images)


@blueprint.route('/card-salon/<salonID>')
def card_salon(salonID):
    salon = Salon.query.filter(Salon.id == salonID).first()
    return render_template('salon/card_salon.html', salon=salon)
