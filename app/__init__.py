from flask import Flask
from app.views.object_detector_view import video_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(video_blueprint, url_prefix='/video')
    app.config.from_object('app.config')

    return app
