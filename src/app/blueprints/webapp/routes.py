from flask import Blueprint, render_template

webapp = Blueprint('webapp', __name__, template_folder='templates')

@webapp.route('/')
def index():
    return render_template('webapp/index.html')