import motion_opencv
import yaml
import time
import emoji
from cv2 import cv2

from recording import record_video
from motion_opencv import motion_detection


CONFIG = None
with open('config.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)
  CONFIG = data

video = cv2.VideoCapture(0)
# print('Adjusting camara lighting')
# time.sleep(2)

start_time = time.time()
canRecord = True
state = None

while True:
  end_time = time.time()

  if(end_time - start_time >= 0):
    canRecord = True
    start_time = time.time()
  # print(state)
  vic = record_video(CONFIG, video)
  print(vic)
  # motion_detection(cv2, video)
  if canRecord == True:
    canRecord = False
