#!/usr/local/bin/python
import requests
import logging
import pdb, json

def api_key():
  with open('/users/smittapalli/.creds/cta_api_key','r') as credfile:
    return credfile.readlines()[0][0:-1]

# endpoints
# gettime
#   - returns the time
# getdirections
#   - returns direction of bus route
#   - example params: "rt=134"
# getstops
#   - returns list of stops, phy address and long/lat
#   - example params: "rt=134&dir=Southbound"
#           # stock & wrightwood => stpid = 1078
# getpredictions
#   - returns list of arrival times for routes and stops
#   - example params: "rt[]=134&rt[]=156&stpid=1078"
#   - can specify only routes or only vehicles or only stops, can specify multiple of each
def v2(endpoint, param_string):
  API_KEY = api_key()
  URL = "http://www.ctabustracker.com/bustime/api/v2/{1}?key={0}&format=json&{2}".format(API_KEY, endpoint, param_string)
  #pdb.set_trace()
  logging.basicConfig(level=logging.INFO)
  logging.info("API call to cta v2 for endpoint {0} with params {1}".format(endpoint, param_string))
  res = requests.get(URL)
  if res.status_code == 200:
    return res.json()
  else:
    return "ERROR"

def next_arrival(busroute, stpid):
  res = v2('getpredictions', "rt={0}&stpid={1}".format(busroute, stpid))
  if res["bustime-response"].keys()[0] == 'error':
    return res["bustime-response"]["error"][0]["msg"]
    #return "error"
  else:
    times = []
    for t in res["bustime-response"]["prd"]:
      #times.append(int(t["prdctdn"]))
      tim = t["prdctdn"] if t["prdctdn"] == "DUE" else int(t["prdctdn"])
      times.append(tim)
    return sorted(times)

def ppjson(da_json):
  print json.dumps(da_json, indent=2, sort_keys=True)

if __name__ == "__main__":
  print 'starting debugging console'
  pdb.set_trace()
