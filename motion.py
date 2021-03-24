#!/usr/bin/env python3.7.3
import RPi.GPIO as GPIO
import time

# Define pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  # Motion seor input
GPIO.setup(3, GPIO.OUT)  # Debugging only


def watchForMotion():
  i = GPIO.input(11)
  shouldRecord = False
  if i == 0:
    GPIO.output(3, 0)  # Debugging only OFF
    time.sleep(1)

  elif i == 1:
    GPIO.output(3, 1)  # Debugging only ON
    time.sleep(1)
    shouldRecord = True
  return shouldRecord
