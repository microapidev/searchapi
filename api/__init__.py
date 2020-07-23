from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from config import Config


#instantiate flask class
app = Flask(__name__)

app.config.from_object(Config)

#creating db object
db = SQLAlchemy(app)
#createing migrate object
migrate = Migrate(app, db)

#seperation of concerns
from api import endpoints, models
