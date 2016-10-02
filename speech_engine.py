def translate_command(command):
  print "you said: {0}".format(command)

  if command == "lights on":
    print 'need to turn on lights'
  elif command == "lights off":
    print 'need to turn off lights'
  else:
    print 'could not decipher command!'
