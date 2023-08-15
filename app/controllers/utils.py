import os
from werkzeug.utils import secure_filename
from app.config import Config


def save_uploaded_video(file):
    filename = secure_filename(file.filename)
    upload_folder = Config.UPLOAD_FOLDER
    video_path = os.path.join(upload_folder, filename)
    file.save(video_path)
    return video_path
