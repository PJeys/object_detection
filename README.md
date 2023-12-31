# Object Detection Web App

This is a Flask-based web application for object detection in videos using the Detectron2 library.

## Features

- Upload a video for object detection.
- Display the detected object classes and scores.

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/PJeys/object_detection.git
   cd object_detection
Install dependencies using anaconda:


```conda env create -f environment_droplet.yml ```
```conda activate object_detection```


Install detectron2 package

```python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'```

Configure the app by setting your configurations in config.py (Or use the existing one).

Run the app using the following command:


```python run.py```

Open your web browser and navigate to http://localhost:5000 to use the app.

## Architecture design

You can check diagram in a file named objectDetectionApp.drawio.png

## Usage

Upload a video file in the web interface.

The app will process the video and display object detection results.

Results include detected object classes and scores.

To use again, reload page
