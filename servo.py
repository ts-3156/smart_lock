import RPi.GPIO as GPIO
import time

gp_out = 18
servo = None

def start():
  global servo
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(gp_out, GPIO.OUT)
  servo = GPIO.PWM(gp_out, 50)
  servo.start(0)
  time.sleep(0.5)

def rotate_0():
  servo.ChangeDutyCycle(2.5)
  time.sleep(0.5)

def rotate_90():
  servo.ChangeDutyCycle(7.25)
  time.sleep(0.5)

def stop():
  global servo
  servo.stop()
  servo = None
  GPIO.cleanup()

def initialize():
  start()
  rotate_0()
  stop()

if __name__ == '__main__':
  initialize()
  rotate_90()
  stop()

