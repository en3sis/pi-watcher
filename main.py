import motion_opencv
import yaml
import time
import emoji
from cv2 import cv2

# Custom functions
from recording import record_video
from libs.cloudinary import upload_file
from motion_opencv import motion_detection

CONFIG = None

with open('config.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)
  CONFIG = data

while True:
  motion_detection(cv2)
  vic = record_video(CONFIG, cv2)
  upload_file(vic, CONFIG)
