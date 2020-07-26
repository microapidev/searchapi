# Application factory
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from src.config import Config, DevelopmentConfig
from flask_marshmallow import Marshmallow

import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)

    # Setup configurations
    app.config.from_object(config_class)

    # Import blueprints   
    from src.app.blueprints.api.endpoints import api
    from src.app.blueprints.webapp.routes import webapp

    # Register blueprints
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(webapp)

    #setup flask instance extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    with app.app_context():
        db.create_all()
    

    return app