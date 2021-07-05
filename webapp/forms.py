from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import InputRequired, Email, EqualTo


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
        'Отправить',
        render_kw={"class": "btn btn-primary"}
    )


class RegistrationForm(FlaskForm):
    email = StringField(
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
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )


class SalonForm(FlaskForm):
    name = StringField(
        'Название салона',
        validators=[InputRequired()]
    )
    number_phone = StringField(
        'Номер телефона',
        validators=[InputRequired()]
    )
    address = StringField(
        'Адрес',
        validators=[InputRequired()],
    )
    email = StringField(
        'Электронная почта',
        validators=[InputRequired(), Email()]
    )


class MasterForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    last_name = StringField(
        'Фамилия',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    city = StringField(
        'Город',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    address = StringField(
        'Адрес',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    number_phone = StringField(
        'Номер телефона',
        validators=[InputRequired()],
        render_kw={"class": "form-control"}
    )
    email = StringField(
        'Электронная почта',
        validators=[InputRequired(), Email()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Завершить регистрацию',
        render_kw={"class": "btn btn-primary"}
    )


class UserForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[InputRequired()]
    )
    last_name = StringField(
        'Фамилия',
        validators=[InputRequired()]
    )
    number_phone = StringField(
        'Номер телефона',
        validators=[InputRequired()]
    )
    email = StringField(
        'Электронная почта',
        validators=[InputRequired(), Email()]
    )
    date_of_birth = DateField(
        'Дата рождения',
        validators=[InputRequired()]
    )
