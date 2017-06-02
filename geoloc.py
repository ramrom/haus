#!/usr/local/bin/python
import requests

with open('/users/smittapalli/.creds/gcloud_geoloc_key','r') as credfile:
  API_KEY = credfile.readlines()[0][0:-1]

URL = "https://www.googleapis.com/geolocation/v1/geolocate?key={0}".format(API_KEY)
resp = requests.post(URL)
print resp.json()
