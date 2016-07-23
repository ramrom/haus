#!  /usr/bin/python
#   Title: samsungremote.py
#   Author: Asif Iqbal
#   Date: 05APR2012
#   Info: To send remote control commands to the Samsung tv over LAN
#   TODO:

import socket
import base64
import time, datetime

#IP Address of TV
tvip = "192.168.1.121"
#IP Address of TV
myip = "100.0.0.112"
#Used for the access control/validation, but not after that AFAIK
mymac = "00-0c-29-3e-b1-4f"
#What the iPhone app reports
appstring = "iphone..iapp.samsung"
#Might need changing to match your TV type
tvappstring = "iphone.UE55C8000.iapp.samsung"
#What gets reported when it asks for permission
remotename = "Python Samsung Remote"

# Function to send keys
def sendKey(skey, dataSock, appstring):
  messagepart3 = chr(0x00) + chr(0x00) + chr(0x00) + chr(len(base64.b64encode(skey))) + chr(0x00) + base64.b64encode(skey);
  part3 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring + chr(len(messagepart3)) + chr(0x00) + messagepart3
  dataSock.send(part3);

# Open Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((tvip, 55000))

# Key Reference
# Normal remote keys
#KEY_0
#KEY_1
#KEY_2
#KEY_3
#KEY_4
#KEY_5
#KEY_6
#KEY_7
#KEY_8
#KEY_9
#KEY_UP
#KEY_DOWN
#KEY_LEFT
#KEY_RIGHT
#KEY_MENU
#KEY_PRECH
#KEY_GUIDE
#KEY_INFO
#KEY_RETURN
#KEY_CH_LIST
#KEY_EXIT
#KEY_ENTER
#KEY_SOURCE
#KEY_AD #KEY_PLAY
#KEY_PAUSE
#KEY_MUTE
#KEY_PICTURE_SIZE
#KEY_VOLUP
#KEY_VOLDOWN
#KEY_TOOLS
#KEY_POWEROFF
#KEY_CHUP
#KEY_CHDOWN
#KEY_CONTENTS
#KEY_W_LINK #Media P
#KEY_RSS #Internet
#KEY_MTS #Dual
#KEY_CAPTION #Subt
#KEY_REWIND
#KEY_FF
#KEY_REC
#KEY_STOP
# Bonus buttons not on the normal remote:
#KEY_TV
#Don't work/wrong codes:
#KEY_CONTENT
#KEY_INTERNET
#KEY_PC
#KEY_HDMI1
#KEY_OFF
#KEY_POWER
#KEY_STANDBY
#KEY_DUAL
#KEY_SUBT
#KEY_CHANUP
#KEY_CHAN_UP
#KEY_PROGUP
#KEY_PROG_UP

# First configure the connection
ipencoded = base64.b64encode(myip)
macencoded = base64.b64encode(mymac)
messagepart1 = chr(0x64) + chr(0x00) + chr(len(ipencoded)) \
+ chr(0x00) + ipencoded + chr(len(macencoded)) + chr(0x00) \
+ macencoded + chr(len(base64.b64encode(remotename))) + chr(0x00) \
+ base64.b64encode(remotename)

part1 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring \
+ chr(len(messagepart1)) + chr(0x00) + messagepart1
sock.send(part1)

messagepart2 = chr(0xc8) + chr(0x00)
part2 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring \
+ chr(len(messagepart2)) + chr(0x00) + messagepart2
sock.send(part2)

# Now send the keys as you like, e.g.,
sendKey("KEY_VOLUP",sock,tvappstring)
time.sleep(1)
sendKey("KEY_TOOLS",sock,tvappstring)
time.sleep(1)
sendKey("KEY_RIGHT",sock,tvappstring)
time.sleep(1)
sendKey("KEY_DOWN",sock,tvappstring)
time.sleep(1)
sendKey("KEY_RIGHT",sock,tvappstring)

# Close the socket when done
sock.close()
