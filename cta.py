#!/usr/local/bin/python
import requests
import pdb

def bus_sched(bus_num, station):
  with open('/users/smittapalli/.creds/cta_api_key','r') as credfile:
    API_KEY = credfile.readlines()[0][0:-1]

  URL = "http://www.ctabustracker.com/bustime/api/v2/gettime?key={0}&format=json".format(API_KEY)
  #pdb.set_trace()
  res = requests.get(URL)
  if res.status_code == 200:
    return res.json()
  else:
    return "ERROR"

if __name__ == "__main__":
  print 'starting debugging console'
  pdb.set_trace()
