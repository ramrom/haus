#!/usr/local/bin/python
import requests
import json, sys
import pdb

def get_city_state(json_r):
  city = json_r['results'][2]['postcode_localities']

def get_long_lat():
  with open('/users/smittapalli/.creds/gcloud_geoloc_key','r') as credfile:
    API_KEY = credfile.readlines()[0][0:-1]

  LONGLAT_URL = "https://www.googleapis.com/geolocation/v1/geolocate?key={0}".format(API_KEY)
  response = requests.post(LONGLAT_URL)
  return response.json()

def get_human_location(longitude, latitude):
  with open('/users/smittapalli/.creds/gcloud_geocode_key','r') as credfile:
    API_KEY2 = credfile.readlines()[0][0:-1]

  ADDRESS_URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={1},{2}&key={0}".format(API_KEY2, longitude, latitude)
  response = requests.post(ADDRESS_URL)
  return response.json()
  #pdb.set_trace()

if __name__ == "__main__":
  print "usage: 1 to print long/lat"
  if len(sys.argv) > 1 and sys.argv[1] == '1':
    response = get_long_lat()
    print response['location']
    #response2 = get_human_location(response['location']['lat'], response['location']['lng'])
    #print json.dumps(response2, indent=4, sort_keys=True)
