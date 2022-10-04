from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DATABASE_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.secret_key = 'oSVXwod41diugXj8Hm00Hw'
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app


def create_database(app):
    if not path.exists('website/' + DATABASE_NAME):
        db.create_all(app=app)
        print('database created')
        print(db.metadata.tables.keys())
