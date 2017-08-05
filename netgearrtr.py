#!/usr/local/bin/python

import pdb
import pynetgear

def buildclient(password = 'password', user = 'admin', hostname = 'routerlogin.net', port = 80):
  return pynetgear.Netgear(password, hostname, user, port)

if __name__ == "__main__":
  #if len(sys.argv) > 1 and sys.argv[1] == '1':
  pdb.set_trace()
