import os
from werkzeug.utils import secure_filename
from flask import current_app


def save_uploaded_video(file):
    filename = secure_filename(file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    video_path = os.path.join(upload_folder, filename)
    file.save(video_path)
    return video_path
