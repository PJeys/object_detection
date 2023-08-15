from flask import Blueprint, request, render_template, jsonify
from app.controllers.object_detector_controller import ObjectDetector

video_blueprint = Blueprint('video', __name__, url_prefix='/video')


@video_blueprint.route('/detect_objects', methods=['GET', 'POST'])
def detect_objects():
    if request.method == 'POST':

        video_file = request.files.get('video')

        object_detector = ObjectDetector()
        results = object_detector.process_video(video_file)
        print(results)
        return jsonify(results), 200

    return render_template('upload.html')
