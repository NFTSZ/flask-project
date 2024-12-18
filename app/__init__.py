from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes.home import index_route
        app.register_blueprint(index_route)

    return app