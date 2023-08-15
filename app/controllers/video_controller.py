from flask import Blueprint, request, jsonify, render_template
from app.models.object_detector import ObjectDetector

video_blueprint = Blueprint('video', __name__, url_prefix='/video')


@video_blueprint.route('/detect_objects', methods=['POST'])
def detect_objects():
    video_file = request.files.get('video')

    if video_file:
        object_detector = ObjectDetector()
        results = object_detector.process_video(video_file)
        return render_template('upload.html', results=results)

    return jsonify({'error': 'No video file provided'}), 400
