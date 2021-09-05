from flask import Flask
from webapp.db import db
from webapp.general.models import Auth

from webapp.general.views import blueprint as generel_blueprint
from webapp.salon.views import blueprint as salon_blueprint
from webapp.master.views import blueprint as master_blueprint
from webapp.user.views import blueprint as user_blueprint

from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

app.register_blueprint(generel_blueprint)
app.register_blueprint(salon_blueprint)
app.register_blueprint(master_blueprint)
app.register_blueprint(user_blueprint)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'general.login'


@login_manager.user_loader
def load_user(user_id):
    return Auth.query.get(user_id)
