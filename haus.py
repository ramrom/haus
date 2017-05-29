#!/usr/local/bin/python

from ouimeaux.environment import Environment
import time
import sys, pdb
import saystuff, weather

def on_switch(switch):
  print "Switch found!", switch.name

def on_motion(motion):
  print "Motion found!", motion.name

# CLI usage: 'wemo switch "TV Room" on'
def toggle_switch(switch):
  current_state = switch.basicevent.GetBinaryState()['BinaryState']
  new_state = '1' if current_state == '0' else '1'
  switch.basicevent.SetBinaryState(BinaryState=new_state)

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == 'light':
    env = Environment(on_switch, on_motion)
    env.start()
    env.discover(seconds=3)
    #time.sleep(2)
    #env.list_switches()
    switch = env.get_switch('ramhalolight')
    switch.blink()
    #toggle_switch(switch)
  else:
    #pdb.set_trace()
    r = weather.yweather()
    phrase = "the temperature is {0} degrees".format(r[u'item'][u'condition'][u'temp'])
    saystuff.gspeak(phrase)
