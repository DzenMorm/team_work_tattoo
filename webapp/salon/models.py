from webapp.db import db


class Salon(db.Model):
    __tablename__ = 'salon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    number_phone = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref='salons')

    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'))
    auth = db.relationship('Auth', backref=db.backref('salon', uselist=False))

    def __repr__(self):
        return f'''<Tattoo Salon {self.name}, {self.address}, {self.email},
                    {self.number_phone}, {self.city_id}, {self.city}>'''
