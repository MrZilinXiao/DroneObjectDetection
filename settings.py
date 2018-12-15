# Muiltiple settings are as follows.
CAM_NUMBER = 0
#MODEL_PATH = './data/model.h5'
#ANCHORS_PATH = './data/anchors.txt'
#CLASSES_PATH = './data/classes.txt'
MODEL_PATH = './trained/yolo_60000.h5'
ANCHORS_PATH = './trained/yolo_anchors.txt'
CLASSES_PATH = './trained/coco_classes.txt'
# Online stream settings are as below.
REMOTE_IP = '192.168.10.233'
RESOLUTION = [1024, 768]
REMOTE_PORT = 7999
FPS = 15
IS_COMPRESSED = False
ONLINE_STREAM_QUALITY = 100
