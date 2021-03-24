#!/usr/bin/env python3.7.3
import time
import yaml

from recording import captureVideo, record_video

CONFIG = ''
with open('config.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)
  CONFIG = data

# Debuging and testing
captureVideo()
# record_video()
