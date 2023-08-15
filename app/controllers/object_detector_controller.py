import cv2
from multiprocessing import Pool
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
import torch
from app.controllers.utils import save_uploaded_video
from tqdm import tqdm


class ObjectDetector:
    def __init__(self):
        self.predictor = DefaultPredictor(self._config_model())

    @staticmethod
    def _config_model():
        cfg = get_cfg()
        cfg.MODEL.DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
        cfg.merge_from_file(model_zoo.get_config_file('COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml'))
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url('COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml')
        return cfg

    def process_frame(self, frame):
        if frame is None:
            return None
        instances = self.predictor(frame)
        serialized_instances = self.serialize_instance(instances)
        return serialized_instances

    def serialize_instance(self, instance):
        class_names = MetadataCatalog.get(self.predictor.cfg.DATASETS.TRAIN[0]).thing_classes
        if len(instance['instances']) > 0:
            serialized_instance = {
                class_names[instance['instances'].pred_classes.tolist()[0]]: instance["instances"].scores.tolist()[0],
            }
            return serialized_instance

    def process_video(self, video_file):
        video_path = save_uploaded_video(video_file)
        cap = cv2.VideoCapture(video_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        results = []
        with Pool(processes=4) as pool, tqdm(total=len(frames)) as pbar:
            for result in pool.imap_unordered(self.process_frame, frames):
                if result:
                    results.append(result)
                pbar.update(1)

        return results
