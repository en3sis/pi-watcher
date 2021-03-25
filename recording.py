#!/usr/bin/env python3.7.3
import time
import emoji

from cv2 import cv2
# from libs.cloudinary import upload_file
# Constants
TIME_STAMP = str(time.time()).replace('.', '')

video = cv2.VideoCapture(0)


def record_video(CONFIG):
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


# Only for DEMO/Debug
def captureVideo(CONFIG):
  cap = cv2.VideoCapture(0)

  while(True):
    # timer = cv2.getTickCount()
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # cv2.putText()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #   video_file = record_video(CONFIG)
    #   upload_file(str(video_file), CONFIG)
    #   print(emoji.emojize(":eye:  Waiting for motion..."))
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()
