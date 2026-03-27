from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login' #new line


# blueprint for auth routes in our app #new blueprint
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-authentication parts of the app
from .task import task as task_blueprint
app.register_blueprint(task_blueprint)

from core import views, models