from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, ValidationError
from .models import Master


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

    def validate_number_phone(self, number_phone):
        count_phone = Master.query.filter_by(
            number_phone=number_phone.data).count()
        if count_phone > 0:
            raise ValidationError('Такой номер телефона уже используется')

    def validate_email(self, email):
        count_email = Master.query.filter_by(email=email.data).count()
        if count_email > 0:
            raise ValidationError('Такой почтовый адрес уже существует')
