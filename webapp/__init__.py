from flask import Flask
from webapp.models import db, Auth

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

from webapp import routes

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Auth.query.get(user_id)
