from flask import Blueprint, render_template

index_route = Blueprint('index', __name__)

@index_route.route('/')
def home():
    return render_template('index.html')

