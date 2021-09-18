from webapp.master.forms import MasterForm
from webapp.general.forms import ImageForm

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from webapp.db import db

from webapp.general.models import City
from webapp.salon.models import Salon
from webapp.master.models import Master

blueprint = Blueprint('master', __name__, url_prefix='/masters')


@blueprint.route('/master-reg')
def master_reg():
    title = 'Регистрация тату-мастера'
    form = MasterForm()
    if current_user.user:
        return redirect(url_for('general.index'))
    elif current_user.master:
        return redirect(url_for('master.profile_master'))
    elif current_user.salon:
        return redirect(url_for('salon.profile_salon'))
    return render_template('login/masterreg.html', page_title=title,
                           form=form)


@blueprint.route('/process-master-reg', methods=['POST'])
def process_master_reg():
    form = MasterForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = City(name=form.city.data)
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
        return redirect(url_for('master.profile_master'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле "{getattr(form, field).label.text}": {error}')
        return redirect(url_for('master.master_reg'))


@blueprint.route('/profile-master')
def profile_master():
    if not current_user.is_authenticated:
        return redirect(url_for('general.index'))
    title = 'Профиль'
    form = ImageForm()
    images = current_user.master.images
    return render_template(
        'master/profile_master.html',
        title=title,
        form=form,
        images=images
    )


@blueprint.route('/card-master/<masterID>')
def card_master(masterID):
    master = Master.query.filter(Master.id == masterID).first()
    return render_template('master/card_master.html', master=master)