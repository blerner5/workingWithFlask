from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import Configuration


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    migrate.init_app(app, db)


    from core.task import task as task_blueprint

    app.register_blueprint(task_blueprint)


    return app
