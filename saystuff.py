#!/usr/local/bin/python

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
def gspeak(phrase = 'hello', language = 'en-uk'):
  tts = gTTS(text=phrase, lang=language)
  tts.save("phrase.mp3")
  os.system("afplay phrase.mp3")
  os.system("rm phrase.mp3")
# gtts-cli.py "Hello" -l 'en' -o hello.mp3
