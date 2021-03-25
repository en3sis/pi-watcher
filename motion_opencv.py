# https://raw.githubusercontent.com/bnbe-club/opencv-object-detection-diy-33/master/basic-motion-detection-avg.py
import time
import numpy as np
import emoji


def motion_detection(cv2):
  video = cv2.VideoCapture(0)
  time.sleep(3)
  avg = None
  areaValue = 0
  print(emoji.emojize(":eye: Looking for motion..."))

  while True:
    check, frame = video.read()

    # convert imags to grayscale &  blur the result
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # inittialize avg if it hasn't been done
    if avg is None:
      avg = gray.copy().astype("float")
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

      if(int(area) > 5000):
        break
      areaValue = area
      cv2.putText(frame, "Largest Contour", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show Area
    cv2.putText(frame, str(int(areaValue)), (0 + 10, 0 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # show the frame
    cv2.imshow("Video", frame)

    # if the 'q' key is pressed then break from the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
      break

  cv2.destroyAllWindows()
