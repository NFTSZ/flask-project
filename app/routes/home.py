from flask import Blueprint, render_template

index_route = Blueprint('index_route', __name__)

@index_route.route('/')
def index():
    return 'ola'

