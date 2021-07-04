from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.core import RadioField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[InputRequired()],
                             render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    email = EmailField(
        "Электронная почта",
        validators=[InputRequired(), Email()],
        render_kw={"class": "form-control"}
    )
    password = PasswordField(
        "Пароль",
        validators=[InputRequired(), EqualTo("password2")],
        render_kw={"class": "form-control"}
    )
    password2 = PasswordField(
        "Повторите пароль",
        render_kw={"class": "form-control"}
    )
    role = RadioField(
        'Выберите форму регистрации',
        choices=[
            ('1', 'Пользователь'),
            ('2', 'Мастер'),
            ('3', 'Тату Салон')
        ],
        validators=[InputRequired()]
    )
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )


class SalonForm(FlaskForm):
    name = StringField('Введите Ваше имя', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    number_phone = StringField('Введите Ваш номер телефона',
                               validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    address = StringField('Введите адресс салона', validators=[InputRequired()],
                          render_kw={"class": "form-control"})
    city = StringField('Введите город', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )


class UserForm(FlaskForm):
    name = StringField('Введите Имя', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    last_name = StringField('Введите Фамилию', validators=[InputRequired()],
                            render_kw={"class": "form-control"})
    number_phone = StringField('Введите номер телефона',
                               validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    date_of_birth = StringField('Введите дату рождения',
                                validators=[InputRequired()],
                                render_kw={"class": "form-control"})
    city = StringField('Введите город', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )
