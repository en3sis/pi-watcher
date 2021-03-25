import motion_opencv
import yaml
import time
import emoji
from cv2 import cv2

from recording import record_video
from libs.cloudinary import upload_file
from motion_opencv import motion_detection


CONFIG = None
with open('config.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)
  CONFIG = data


# print('Adjusting camara lighting')
# time.sleep(2)

# start_time = time.time()

# global canRecord
# canRecord = True


while True:
  # end_time = time.time()

  # if(end_time - start_time >= 60):
  #   canRecord = True
  #   start_time = time.time()

  motion_detection(cv2)
  vic = record_video(CONFIG, cv2)
  upload_file(vic, CONFIG)
  # if canRecord == True:
  #   canRecord = False

  # print(vic)
