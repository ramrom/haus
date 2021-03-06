# Weather
import requests
import pdb # type 'h' for help
import logging

# to reload a module do "reload(module)"

def yweather():
  #'https://query.yahooapis.com/v1/public/yql?q=\'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="chicago, il")\'&format=json'
  #url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22chicago%2C%20il%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
  logging.basicConfig(level=logging.INFO)
  city = 'chicago'
  state = 'il'
  url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{0}%2C%20{1}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(city, state)


  #query = "select * from weather.forecast where woeid in (SELECT woeid FROM geo.places WHERE text=\"({lat},{lon})\")".format(longitude, lat)
  #url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{0}%2C%20{1}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(41.92, -87.64)

  #url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.placefinder%20where%20text%3D%2239.0618491343%2C-96.5917968750%22%20and%20gflags%20%3D%20%22R%22)%20and%20u=%22c%22&format=json&diagnostics=true&callback="

  res = requests.get(url)
  if res.status_code == 200:
    res_json = res.json()
    #pdb.set_trace()
    if res_json[u'query'][u'results'] == None:
      logging.warning("no results found")
    else:
      logging.info("successfully retrieved weather info from yahoo")
      return res_json[u'query'][u'results'][u'channel'] #[u'item'][u'forecast']
  else:
    logging.error("failed to retrieve data from yahoo, status code: {0}".format(res.status_code))
