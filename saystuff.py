#!/usr/bin/python

from espeak import espeak
import time

espeak.synth('hello world')
time.sleep(2)
