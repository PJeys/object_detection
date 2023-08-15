from flask import Flask
from app.controllers.video_controller import video_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(video_blueprint, url_prefix='/video')
    app.config.from_object('app.config')

    return app
