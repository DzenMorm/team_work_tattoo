from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, MultipleFileField
from wtforms.fields.html5 import EmailField
from wtforms.fields.core import RadioField
from wtforms.validators import InputRequired, Email, EqualTo, ValidationError

from webapp.general.models import Auth


class LoginForm(FlaskForm):
    email = StringField(
        'Электронная почта',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    password = PasswordField(
        'Пароль',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Войти',
        render_kw={"class": "btn btn-primary"}
    )


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

    def validate_email(self, email):
        count_email = Auth.query.filter_by(email=email.data).count()
        if count_email > 0:
            raise ValidationError('Такая почта уже существует')


class ImageForm(FlaskForm):
    image = MultipleFileField(
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Загрузить',
        render_kw={"class": "btn btn-primary"}
    )


class SearchCityForm(FlaskForm):
    city = StringField(
        'Город',
        validators=[InputRequired()],
        render_kw={
            "class": "form-control",
            'placeholder': 'Введите город'
        }
    )
    submit = SubmitField(
        'Найти',
        render_kw={"class": "btn btn-primary"}
    )