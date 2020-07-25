from flask import Flask, render_template, jsonify, make_response, Blueprint
from src.app import  db
import json
import datetime


#Endpoints/routes
api = Blueprint('api', __name__)
    
@api.route("/hello")
def index():
    return "hello world"


