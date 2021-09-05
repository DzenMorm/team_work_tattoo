from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired


class MasterForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    last_name = StringField('Фамилию', validators=[InputRequired()],
                            render_kw={"class": "form-control"})
    number_phone = StringField('Номер телефона',
                               validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    address = StringField('Адрес',
                          validators=[InputRequired()],
                          render_kw={"class": "form-control"})
    email = EmailField('Электронная почта',
                       validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    salon = StringField('Введите салон в котором работаете (если есть)',
                        render_kw={"class": "form-control"})
    city = StringField('Город', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )
