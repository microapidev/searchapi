# Application factory
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from config import Config
from flask_marshmallow import Marshmallow

#instantiate flask class
app = Flask(__name__)

app.config.from_object(os.environ['FLASK_ENV'])

#creating db object
db = SQLAlchemy(app)
#createing migrate object
migrate = Migrate(app, db)

ma = Marshmallow(app)

#seperation of concerns
from api import endpoints, models
