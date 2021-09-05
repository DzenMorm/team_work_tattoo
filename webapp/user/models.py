from webapp.db import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    number_phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref='users')

    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'))
    auth = db.relationship('Auth', backref=db.backref('user', uselist=False))

    def __repr__(self):
        return f'''<User {self.name}, {self.last_name}, {self.email},
                    {self.number_phone}>'''
