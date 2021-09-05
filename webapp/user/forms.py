from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import InputRequired


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
