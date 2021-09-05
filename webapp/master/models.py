from webapp.db import db


class Master(db.Model):
    __tablename__ = 'master'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    number_phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)

    salon_id = db.Column(db.Integer, db.ForeignKey('salon.id'),
                         nullable=True)
    salon = db.relationship('Salon', backref='masters')

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'),
                        nullable=True)
    city = db.relationship('City', backref='masters')

    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'))
    auth = db.relationship('Auth', backref=db.backref('master', uselist=False))

    def __repr__(self):
        return f'''<Tattoo Master {self.name}, {self.last_name}, {self.email},
                    {self.number_phone}>'''
