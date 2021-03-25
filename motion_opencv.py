# https://raw.githubusercontent.com/bnbe-club/opencv-object-detection-diy-33/master/basic-motion-detection-avg.py
import time
from cv2 import cv2
import numpy as np
import yaml
import emoji
from recording import record_video
from libs.cloudinary import upload_file
import threading

CONFIG = None
with open('config.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)
  CONFIG = data

video = cv2.VideoCapture(0)
print('Adjusting camara lighting')
# time.sleep(6)


avg = None

print(emoji.emojize(":eye:  Waiting for motion..."))

while True:
  def recordAndUpload():
    video_file = record_video(CONFIG, video, cv2)
    return print(video_file)
    # upload_file(str(video_file), CONFIG)
    # print(emoji.emojize(":eye:  Waiting for motion..."))

  secThread = threading.Thread(target=recordAndUpload)

  check, frame = video.read()
  # convert imags to grayscale &  blur the result
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (21, 21), 0)

  # inittialize avg if it hasn't been done
  if avg is None:
    avg = gray.copy().astype("float")
    # rawCapture.truncate(0)
    continue

  # accumulate the weighted average between the current frame and
  # previous frames, then compute the difference between the current
  # frame and running average
  cv2.accumulateWeighted(gray, avg, 0.05)
  frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

  # coonvert the difference into binary & dilate the result to fill in small holes
  thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
  thresh = cv2.dilate(thresh, None, iterations=2)

  # show the result
  cv2.imshow("Delta + Thresh", thresh)

  # find contours or continuous white blobs in the image
  contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  # find the index of the largest contour
  if len(contours) > 0:
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]

    # draw a bounding box/rectangle around the largest contour
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    area = cv2.contourArea(cnt)

    # print area to the terminal
    print(area)

    if secThread.is_alive() == False:
      if (area > 4000) & (area < 5000):
        print(emoji.emojize(":bird: Motion detected"))
        secThread.start()
        secThread.join()
      # continue

    # add text to the frame
    cv2.putText(frame, "Largest Contour", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

  # show the frame
  cv2.imshow("Video", frame)

  # if the 'q' key is pressed then break from the loop
  key = cv2.waitKey(1) & 0xFF
  if key == ord('q'):
    break

cv2.destroyAllWindows()
