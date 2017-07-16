#!/usr/local/bin/python
import requests
import logging
import json, sys
import pdb

def get_city_state(json_r):
  city = json_r['results'][2]['postcode_localities']

def long_lat():
  with open('/users/smittapalli/.creds/gcloud_geoloc_key','r') as credfile:
    API_KEY = credfile.readlines()[0][0:-1]

  LONGLAT_URL = "https://www.googleapis.com/geolocation/v1/geolocate?key={0}".format(API_KEY)

  logging.basicConfig(level=logging.INFO)
  logging.info("API call to google geolocate for long/lat")
  response = requests.post(LONGLAT_URL)
  return response.json()

def human_location(longitude, latitude):
  with open('/users/smittapalli/.creds/gcloud_geocode_key','r') as credfile:
    API_KEY2 = credfile.readlines()[0][0:-1]

  ADDRESS_URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={1},{2}&key={0}".format(API_KEY2, longitude, latitude)

  logging.basicConfig(level=logging.INFO)
  logging.info("API call to google geocode for human addresses")
  response = requests.post(ADDRESS_URL)
  return response.json()
  #pdb.set_trace()

if __name__ == "__main__":
  print "usage: 1 to print long/lat"
  if len(sys.argv) > 1 and sys.argv[1] == '1':
    response = long_lat()
    print response['location']
    #response2 = get_human_location(response['location']['lat'], response['location']['lng'])
    #print json.dumps(response2, indent=4, sort_keys=True)
  else:
    print 'starting debugging console'
    pdb.set_trace()
