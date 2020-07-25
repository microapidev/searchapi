from flask import Flask, render_template, jsonify, make_response, Blueprint
from searchapi import app, db
import json
import datetime


#Endpoints/routes
api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.routes
    



