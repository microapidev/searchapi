from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return '<h1> Hello World </h1>'