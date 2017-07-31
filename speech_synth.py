#!/usr/local/bin/python
import os

# ESPEAK CODE
#from espeak import espeak
#import time
from gtts import gTTS
import logging
import pdb
#
#espeak.synth('hello world')
#time.sleep(2)

import pyttsx
def pspeak(phrase = 'hello'):
  engine = pyttsx.init()
  engine.say(phrase)
  engine.runAndWait()

def gspeak(phrase = 'hello', language = 'en-uk'):
  logging.basicConfig(level=logging.INFO)
  logging.info("making a call to google to grab text to speech")
  tts = gTTS(text=phrase, lang=language)
  tts.save("phrase.mp3")
  #pdb.set_trace()
  if os.uname()[0] == 'Darwin':
    os.system("afplay phrase.mp3")
  else:
    os.system("omxplayer phrase.mp3")
    #os.system("aplay phrase.mp3")
    #print 'this isnt OSX'
  os.system("rm phrase.mp3")
# gtts-cli.py "Hello" -l 'en' -o hello.mp3

if __name__ == "__main__":
  print 'debug console'
  #if len(sys.argv) > 1 and sys.argv[1] == '1':
  pdb.set_trace()
