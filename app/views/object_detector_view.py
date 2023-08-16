from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from app.controllers.object_detector_controller import ObjectDetector

video_blueprint = Blueprint('video', __name__)


@video_blueprint.route('/detect_objects', methods=['GET', 'POST'])
def detect_objects():
    if request.method == 'POST':

        video_file = request.files.get('video')

        object_detector = ObjectDetector()
        results = object_detector.process_video(video_file)
        return jsonify(results), 200

    return render_template('upload.html')


@video_blueprint.route('/', methods=['GET'])
def index():
    # This route just for test task, it'll make easier to navigate to needed url
    return redirect(url_for('video.detect_objects'))
