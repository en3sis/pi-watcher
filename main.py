#!/usr/bin/env python3.7.3
import time
import yaml
import emoji

from libs.cloudinary import upload_file
from motion import watchForMotion
from record import captureVideo, record_video

CONFIG = ''
with open('config.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)
  CONFIG = data

print(emoji.emojize(":eye: Waiting for motion..."))
while True:
  status = watchForMotion()
  if status == True:
    print(emoji.emojize(":bird: Motion detected"))
    video_file = record_video(CONFIG)
    upload_file(str(video_file), CONFIG)
    print(emoji.emojize(":eye: Waiting for motion..."))

# Debuging and testing
# captureVideo()
# record_video()
