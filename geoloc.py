#!/usr/local/bin/python
import requests
import json
import pdb

with open('/users/smittapalli/.creds/gcloud_geoloc_key','r') as credfile:
  API_KEY = credfile.readlines()[0][0:-1]

LONGLAT_URL = "https://www.googleapis.com/geolocation/v1/geolocate?key={0}".format(API_KEY)
resp = requests.post(LONGLAT_URL)
resp_cont = resp.json()

with open('/users/smittapalli/.creds/gcloud_geocode_key','r') as credfile:
  API_KEY2 = credfile.readlines()[0][0:-1]

#pdb.set_trace()
ADDRESS_URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={1},{2}&key={0}".format(API_KEY2, resp_cont['location']['lat'], resp_cont['location']['lng'])
resp2 = requests.post(ADDRESS_URL)
#pdb.set_trace()
print json.dumps(resp2.json(), indent=4, sort_keys=True)
