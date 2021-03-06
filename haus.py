#!/usr/local/bin/python
import time
import sys, pdb
import speech_synth

#import subprocess
#task = subprocess.Popen("cat file.log | tail -1", shell=True, stdout=subprocess.PIPE)
#data = task.stdout.read()

def load_config():
  import yaml
  with open('config.yml','r') as stream:
    config = yaml.load(stream)
  return config

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1] == 'light':
      import wemo
      wemo.toggle_switch('ramhalolight')
    elif sys.argv[1] == 'cta':
      import cta
      res = cta.next_arrival(151, 1078)
      if res.count("DUE") > 0:
        phrase = "the next arrival of route 151 is due now".format(res[0])
      else:
        phrase = "the next arrival of route 151 is {0} minutes".format(res[0])
      speech_synth.gspeak(phrase)
    elif sys.argv[1] == 'weather':
      import weather
      res = weather.yweather()
      phrase = "the temperature is {0} degrees".format(res[u'item'][u'condition'][u'temp'])
      #pdb.set_trace()
      speech_synth.gspeak(phrase)
  else:
    print 'starting debugging console'
    pdb.set_trace()





#import subprocess  # this is the more modern python 2.6+ way to make external process scripts
#def get_sys_out(command)
#  proc = subprocess.Popen(command, stdout=subprocess.PIPE)
#  return proc.stdout.read()
