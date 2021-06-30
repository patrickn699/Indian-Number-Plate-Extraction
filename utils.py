from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2 import model_zoo
import matplotlib.pyplot as plt
import cv2
from get_num_plate import get_number_plate
import numpy as np
import os
from PIL import Image


class Load_model:

    def load_model(self):
        cfg = get_cfg()
        # cfg.merge_from_file(model_zoo.get_config_file('COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml'))
        cfg.merge_from_file("./config.yaml")
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.75  # Threshold
        cfg.MODEL.WEIGHTS = "./model_final.pth"
        # cfg.MODEL.WEIGHTS = "https://dl.fbaipublicfiles.com/detectron2/COCO-Detection/faster_rcnn_R_101_FPN_3x/137851257/model_final_f6e8b1.pkl"
        cfg.MODEL.DEVICE = "cuda"
        return cfg

    def predict(self, img, cfg):
        #imgg = cv2.imread(img)
        imgg = Image.open(img)
        imgg = np.array(imgg)
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7  # set a custom testing threshold
        predictor = DefaultPredictor(cfg)
        outputs = predictor(imgg)
        return outputs, imgg

    def visulize(self,image, cfg, outputs):

        v = Visualizer(image[:, :, ::-1],
                       metadata=MetadataCatalog.get(cfg.DATASETS.TRAIN[0]),  # building_metadata,
                       scale=0.5,
                       instance_mode=ColorMode.IMAGE
                       # remove the colors of unsegmented pixels. This option is only available for segmentation models
                       )
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

        #plt.matshow(out.get_image()[:, :, ::-1])
        #plt.show()


        #gt.run_easy_ocr(outputs, image)
        return out.get_image()[:, :, ::-1]


        


if __name__ == '__main__':

    l = Load_model()
    gt = get_number_plate()
    cfg = l.load_model()
    op, img = l.predict(os.path.join('Images', '47.jpg'), cfg)
    l.visulize(img, cfg, op)






