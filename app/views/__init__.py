from app.views.object_detector_view import video_blueprint


def init_app(app):
    app.register_blueprint(video_blueprint)
