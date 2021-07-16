from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, MultipleFileField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.fields.core import RadioField
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


class SalonForm(FlaskForm):
    name = StringField('Название Салона', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    number_phone = StringField('Номер телефона',
                               validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    address = StringField('Адресс салона',
                          validators=[InputRequired()],
                          render_kw={"class": "form-control"})
    email = EmailField('Электронная почта', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    city = StringField('Город', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )


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


class MasterForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired()],
                       render_kw={"class": "form-control"})
    last_name = StringField('Фамилию', validators=[InputRequired()],
                            render_kw={"class": "form-control"})
    number_phone = StringField('Номер телефона',
                               validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    address = StringField('Адресс',
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


class ImageForm(FlaskForm):
    image = MultipleFileField(
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