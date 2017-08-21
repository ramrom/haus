#!/usr/local/bin/python
# NOTE: 
# For pi 3 (on ubuntumate) for python 2.7 to install pybluez package
# sudo apt-get install libbluetooth-dev
# sudo pip install pybluez 

import pdb
import bluetooth

# simple inquiry
def bt_devs():
  nearby_devices = bluetooth.discover_devices(lookup_names=True)
  print("found %d devices" % len(nearby_devices))
  
  for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))

# bluetooth low energy scan
  def btle_devs():
  from bluetooth.ble import DiscoveryService
  
  service = DiscoveryService()
  devices = service.discover(2)
  
  for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))

if __name__ == '__main__':
  pdb.set_trace()
  #main()
