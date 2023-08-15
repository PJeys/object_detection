from flask import Flask
from app.views import init_app


def create_app():
    app = Flask(__name__)
    init_app(app)
    app.config.from_object('app.config')

    return app
