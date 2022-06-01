from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config
from newsapi import NewsApiClient
  


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)
    
    with application.app_context():
    	db.init_app(application)
    	bcrypt.init_app(application)
    	login_manager.init_app(application)
    	mail.init_app(application)

    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors

    application.register_blueprint(users)
    application.register_blueprint(posts)
    application.register_blueprint(main)
    application.register_blueprint(errors)


    return application
