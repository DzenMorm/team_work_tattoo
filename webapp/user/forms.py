from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import InputRequired, ValidationError
from .models import User


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    last_name = StringField('Фамилия', validators=[InputRequired()],
                            render_kw={"class": "form-control"})
    number_phone = StringField('Номер телефона',
                               validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    email = EmailField('Электронная почта', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    date_of_birth = DateField('Введите дату рождения',
                              validators=[InputRequired()],
                              format='%Y-%m-%d',
                              render_kw={"class": "form-control"})
    city = StringField('Город', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )

    def validate_number_phone(self, number_phone):
        count_number_phone = User.query.filter_by(number_phone=number_phone.data).count()
        if count_number_phone > 0:
            raise ValidationError('Такой номер уже используется')

    def validate_email(self, email):
        count_email = User.query.filter_by(email=email.data).count()
        if count_email > 0:
            raise ValidationError('Такой почтовый адрес уже существует')
