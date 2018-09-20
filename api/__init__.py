# api/__init__.py

from flask import Blueprint, render_template

api = Blueprint('api', __name__, template_folder='api/templates/')

@api.route('/')
def index():
    return 'api index'

@api.route('/sub')
def sub():
    return 'api sub'
