from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Auth(db.Model, UserMixin):
    __tablename__ = 'auth'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Auth {self.id}, {self.email}>'


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<City {self.name}>'


class Salon(db.Model):
    __tablename__ = 'salon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    number_phone = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    city_id = db.Column(db.Integer, db.ForeignKey(City.id), nullable=False)
    city = db.relationship('City', backref='salons')

    auth_id = db.Column(db.Integer, db.ForeignKey(Auth.id))
    auth = db.relationship('Auth', backref=db.backref('salon', uselist=False))

    def __repr__(self):
        return f'''<Tattoo Salon {self.name}, {self.address}, {self.email},
                    {self.number_phone}>'''


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    number_phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)

    city_id = db.Column(db.Integer, db.ForeignKey(City.id), nullable=False)
    city = db.relationship('City', backref='users')

    auth_id = db.Column(db.Integer, db.ForeignKey(Auth.id))
    auth = db.relationship('Auth', backref=db.backref('user', uselist=False))

    def __repr__(self):
        return f'''<User {self.name}, {self.last_name}, {self.email},
                    {self.number_phone}>'''


class Master(db.Model):
    __tablename__ = 'master'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    number_phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)

    salon_id = db.Column(db.Integer, db.ForeignKey(Salon.id),
                         nullable=True)
    salon = db.relationship('Salon', backref='masters')

    city_id = db.Column(db.Integer, db.ForeignKey(City.id),
                        nullable=False)
    city = db.relationship('City', backref='masters')

    auth_id = db.Column(db.Integer, db.ForeignKey(Auth.id))
    auth = db.relationship('Auth', backref=db.backref('master', uselist=False))

    def __repr__(self):
        return f'''<Tattoo Master {self.name}, {self.last_name}, {self.email},
                    {self.number_phone}>'''


class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    text = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id),
                        nullable=False)
    user = db.relationship('User', backref='reviews')

    master_id = db.Column(db.Integer, db.ForeignKey(Master.id),
                          nullable=True)
    master = db.relationship('Master', backref='reviews')

    salon_id = db.Column(db.Integer, db.ForeignKey(Salon.id),
                         nullable=True)
    salon = db.relationship('Salon', backref='reviews')

    def __repr__(self):
        return f'<Reviews {self.date}, {self.text}>'


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    path = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)

    master_id = db.Column(db.Integer, db.ForeignKey(Master.id),
                          nullable=True)
    master = db.relationship('Master', backref='images')

    salon_id = db.Column(db.Integer, db.ForeignKey(Salon.id),
                         nullable=True)
    salon = db.relationship('Salon', backref='images')

    review_id = db.Column(db.Integer, db.ForeignKey(Review.id),
                          nullable=True)
    review = db.relationship('Review', backref='images')

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    user = db.relationship('User', backref='images')

    def __repr__(self):
        return f'<Drawings and photos {self.name}, {self.description}>'
