#!/usr/local/bin/python
from ouimeaux.environment import Environment
import pdb

def on_switch(switch):
  print "Switch found!", switch.name

def on_motion(motion):
  print "Motion found!", motion.name

def list_switches():
  env = Environment(on_switch, on_motion)
  env.start()
  env.discover(seconds=1)
  return env.list_switches()

def get_switch_state(switch_name):
  env = Environment(on_switch, on_motion)
  env.start()
  env.discover(seconds=1)
  #time.sleep(2)
  switch = env.get_switch(switch_name)
  return switch.basicevent.GetBinaryState()['BinaryState']

def toggle_switch(switch_name):
  env = Environment(on_switch, on_motion)
  env.start()
  env.discover(seconds=1)
  #time.sleep(2)
  switch = env.get_switch(switch_name)
  switch.blink()
  #toggle_switch(switch)

def toggle_switch_dumb(switch):
  current_state = switch.basicevent.GetBinaryState()['BinaryState']
  new_state = '1' if current_state == '0' else '1'
  switch.basicevent.SetBinaryState(BinaryState=new_state)

if __name__ == "__main__":
  print 'starting wemo debugging console'
  pdb.set_trace()
