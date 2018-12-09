import RPi.GPIO as GPIO
import time

gp_out = 18
servo = None

def start():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(gp_out, GPIO.OUT)
  servo = GPIO.PWM(gp_out, 50)
  servo.start(0)

def rotate_90():
  servo.ChangeDutyCycle(2.5)
  time.sleep(0.5)

def stop():
  servo.stop()
  servo = None
  GPIO.cleanup()

if __name__ == '__main__':
  start()
  rotate_90()
  stop()

