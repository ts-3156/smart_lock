#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import nfc
import time
from threading import Thread, Timer
import sys

# Original -> https://qiita.com/undo0530/items/89540a03252e2d8f291b

TIME_cycle = 1.0
TIME_interval = 0.2
TIME_wait = 3

# 212F == FeliCa
target_req_suica = nfc.clf.RemoteTarget("212F")
# 0003 == Suica
target_req_suica.sensf_req = bytearray.fromhex("0000030000")

def print_if_touched()
  clf = nfc.ContactlessFrontend('usb')
  target_res = clf.sense(target_req_suica, iterations=int(TIME_cycle//TIME_interval)+1 , interval=TIME_interval)

  if target_res == None:
    clf.close()
    return

  tag = nfc.tag.activate_tt3(clf, target_res)
  tag.sys = 3

  idm = binascii.hexlify(tag.idm)
  print 'Suica detected. idm = ' + idm
  sys.stdout.flush()
  clf.close()

print 'Suica waiting...'
sys.stdout.flush()

while True:
  print_if_touched()
  print 'sleep ' + str(TIME_wait) + ' seconds'
  sys.stdout.flush()
  time.sleep(TIME_wait)

