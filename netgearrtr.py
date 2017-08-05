#!/usr/local/bin/python

import pdb
import pynetgear   # https://github.com/balloob/pynetgear

# do dir(object) to get list of public methods

def buildclient(password = 'password', user = 'admin', hostname = 'routerlogin.net', port = 80):
  return pynetgear.Netgear(password, hostname, user, port)

if __name__ == "__main__":
  pdb.set_trace()
  # client = buildclient()
  # client.get_attached_devices()
