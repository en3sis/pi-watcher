#!/usr/bin/env python3.7.3
import time
import emoji

from cv2 import cv2

# Constants
TIME_STAMP = str(time.time()).replace('.', '')


def record_video(CONFIG, video):
  cap = video
  # TODO: Update the frame rate/resolution
  # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
  # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

  # Define the codec and create VideoWriter object
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(CONFIG["clip_folder"] + TIME_STAMP + '.avi', fourcc, 20.0, (640, 480))

  # Set the clip length
  currentTimeStap = time.time()
  future = currentTimeStap + CONFIG["clip_length"]

  print(emoji.emojize(":red_circle: Recording..."))
  while time.time() < future:
    if cap.isOpened():

      ret, frame = cap.read()
      if ret == True:
        frame = cv2.flip(frame, 180)
        # write the flipped frame
        out.write(frame)
        # cv2.imshow('frame', frame)

  # Release everything if job is finished
  cap.release()
  out.release()
  cv2.destroyAllWindows()

  return CONFIG["clip_folder"] + TIME_STAMP + '.avi'
