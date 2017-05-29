#!/usr/bin/python

# ESPEAK CODE
#from espeak import espeak
#import time
#
#espeak.synth('hello world')
#time.sleep(2)

import pyttsx
def pspeak():
  engine = pyttsx.init()
  engine.say('Good morning.')
  engine.runAndWait()

from gtts import gTTS
import os
def gspeak():
  tts = gTTS(text='Good morning', lang='en')
  tts.save("good.mp3")
  os.system("mpg321 good.mp3")
# gtts-cli.py "Hello" -l 'en' -o hello.mp3
