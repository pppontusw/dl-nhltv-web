import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)
    from app import models

    return app

