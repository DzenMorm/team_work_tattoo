from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[InputRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[InputRequired(), Email()],
        render_kw={"class": "form-control"}
    )
    password = PasswordField(
        "Пароль",
        validators=[InputRequired(), EqualTo("repeat_password")],
        render_kw={"class": "form-control"}
    )
    repeat_password = PasswordField(
        "Повторите пароль",
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    ) 
