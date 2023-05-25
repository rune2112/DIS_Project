from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#db = "dbname='postgres' user='postgres' host='127.0.0.1' password = 'postgresPassword'"
db = "dbname='DIS_Project' user='postgres' host='127.0.0.1' password = 'DISProjectPass'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)

sessionDetails = {"username": None, "id": None}

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#login_manager.init_app(app=app)

from shop.Login.routes import Login
from shop.User.routes import User
app.register_blueprint(Login)
app.register_blueprint(User)