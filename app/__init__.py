from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes.home import index_route
        from .routes.produtos import product_route
        app.register_blueprint(index_route)
        app.register_blueprint(product_route, url_prefix='/produtos')

    return app