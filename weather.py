# Weather
import requests
import pdb # type 'h' for help

# to reload a module do "reload(module)"

def yahoo_weather():
  #'https://query.yahooapis.com/v1/public/yql?q=\'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="chicago, il")\'&format=json'
  #url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22chicago%2C%20il%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
  city = 'chicago'
  state = 'il'
  url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{0}%2C%20{1}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(city, state)
  res = requests.get(url)
  res_json = res.json()
  forecast = res_json[u'query'][u'results'][u'channel'][u'item'][u'forecast']
  #pdb.set_trace()
  return res.status_code
