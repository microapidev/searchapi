# Application factory
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from config import Config
from flask_marshmallow import Marshmallow
from .api.endpoints import api
from .webapp.routes import webapp

#instantiate flask class
app = Flask(__name__)

#register blueprints
app.register_blueprint(api)
app.register_blueprint(site)

app.config.from_object(os.environ['FLASK_ENV'])

#creating db object
db = SQLAlchemy(app)
#createing migrate object
migrate = Migrate(app, db)

ma = Marshmallow(app)

#seperation of concerns
from api import endpoints
from models import models
