#!/usr/bin/env python

import servo
import suica

if __name__ == '__main__':
  my_idm = os.getenv("IDM", "Not set")
  print 'My idm = ' + my_idm
  sys.stdout.flush()

  servo.initialize()
  suica.initialize()

  while True:
    idm = suica.read()
    if idm == my_idm:
      servo.start()
      servo.rotate_0()
      servo.rotate_90()
      servo.rotate_0()
      servo.stop()
    time.sleep(1)

