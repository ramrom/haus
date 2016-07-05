from ouimeaux.environment import Environment
import time

def on_switch(switch):
  print "Switch found!", switch.name

def toggle_switch(switch):
  current_state = switch.basicevent.GetBinaryState()['BinaryState']
  new_state = '1' if current_state == '0' else '1'
  switch.basicevent.SetBinaryState(BinaryState=new_state)

if __name__ == "__main__":
  env = Environment()
  env.start()
  env.discover(seconds=3)
  #time.sleep(2)
  #env.list_switches()
  switch = env.get_switch('ramhalolight')
  switch.blink()
  #toggle_switch(switch)
