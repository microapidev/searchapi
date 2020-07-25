from flask import Blueprint, jsonify, request, make_response
from src.app import db
from flask import current_app

from src.app.models.models import Movies


api = Blueprint('api',__name__)
 
