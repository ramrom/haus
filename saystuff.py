#!/usr/local/bin/python
import os

# ESPEAK CODE
#from espeak import espeak
#import time
#
#espeak.synth('hello world')
#time.sleep(2)

import pyttsx
def pspeak(phrase = 'hello'):
  engine = pyttsx.init()
  engine.say(phrase)
  engine.runAndWait()

from gtts import gTTS
def gspeak(phrase = 'hello', language = 'en-uk'):
  tts = gTTS(text=phrase, lang=language)
  tts.save("phrase.mp3")
  if os.uname()[0] == 'Darwin':
    os.system("afplay phrase.mp3")
  else:
    print 'this isnt OSX' 
  os.system("rm phrase.mp3")
# gtts-cli.py "Hello" -l 'en' -o hello.mp3

