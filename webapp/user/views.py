from webapp.user.forms import UserForm

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from webapp.db import db

from webapp.general.models import City
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/user-reg')
def user_reg():
    form = UserForm()
    title = 'Регистрация пользователя'
    if current_user.user:
        return redirect(url_for('general.index'))
    elif current_user.master:
        return redirect(url_for('master.profile_master'))
    elif current_user.salon:
        return redirect(url_for('salon.profile_salon'))
    return render_template('login/userreg.html', page_title=title,
                           form=form)


@blueprint.route('/process-user-reg', methods=['POST'])
def process_user_reg():
    form = UserForm()
    if form.validate_on_submit():
        city = City.query.filter(City.name == form.city.data).first()
        if not city:
            city = City(name=form.city.data)
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

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('general.index'))
    return redirect(url_for('general.index'))


# @blueprint.route('/profile-user')
# def profile_user():
#     return render_template('profile_user.html')