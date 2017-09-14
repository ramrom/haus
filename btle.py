#!/usr/local/bin/python
# NOTE: 
# For pi 3 (on ubuntumate) for python 2.7 to install pybluez package
# sudo apt-get install libbluetooth-dev
# sudo pip install pybluez ((aka BlueZ, the official linux bluetooth protocol stack))

import pdb
import bluetooth

# simple inquiry
def bt_devs():
  nearby_devices = bluetooth.discover_devices(lookup_names=True)
  print("found %d devices" % len(nearby_devices))
  
  for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))

# TODO: i sometimes get this, fix it:
#   "*** OSError: [Errno 19] No such device"

# bluetooth low energy scan
# fails with "gattlib not found"
#   - "pip install gattlib" fails b/c glib-2.0 not found
#     - "sudp apt-get install libglib2.0-dev"   
#     - still fails, "fatal error: boost/python/list.hpp: No such file or directory"
#     - did "sudo apt-get install libboost-python-dev"
#     - still fails, lboost_thread not found
#       - see https://raspberrypi.stackexchange.com/questions/55530/pybluez-and-gattlib-error
#     - installed libboost-thread-dev
#   - needs root, i get "Set scan parameters failed (are you root?)" error
# 
# also see https://home-assistant.io/components/device_tracker.bluetooth_le_tracker/

# Flower care, address: C4:7C:8D:62:DE:8B
def btle_devs():
  from bluetooth.ble import DiscoveryService
  
  service = DiscoveryService()
  devices = service.discover(4)
  return devices

def btle_scan():
  from bluetooth.ble import BeaconService

  service = BeaconService()
  devices = service.scan(4)
  return devices
  
  #for address, data in list(devices.items()):
  #  b = Beacon(data, address)
  #  print(b)

def print_btle_devs(devices):
  for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))

if __name__ == '__main__':
  pdb.set_trace()
