#!/usr/local/bin/python

# NOTES:
# forming a request: https://cloud.google.com/speech/docs/sync-recognize#speech-sync-recognize-protocol
# - google speech requires mono channel audio

import pdb, logging, time

def apikey(speech_file_path = '../Documents/test_recording.flac', body = None):
  import base64
  import requests

  with open('/users/smittapalli/.creds/gcloud_base_api_key','r') as credfile:
    API_KEY = credfile.readlines()[0][0:-1]

  URL = 'https://speech.googleapis.com/v1/speech:recognize?key={0}'.format(API_KEY)

  start = time.time()
  with open(speech_file_path, 'rb') as speech:
    speech_content = base64.b64encode(speech.read())

  logging.basicConfig(level=logging.INFO)
  logging.info("opened and encoded {0}, duration: {1}".format(speech_file_path, time.time() - start))
  start = time.time()

  if body == None:
    body={
      'config': {
        #'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
        #'sampleRate': 16000,  # 16 khz
        'languageCode': 'en-US'  # a BCP-47 language tag
      },
      'audio': {
        #'content': speech_content.decode('UTF-8')
        'content': speech_content
        }
      }

  response = requests.post(URL, json = body) 
  logging.info("POST request to google speech api done, duration: {0}".format(time.time() - start))
  res = response.json()
  # res['results'][0]['alternatives'][0]['transcript']  # the actual translation
  # res['results'][0]['alternatives'][0]['confidence']  # confidence level of accuracy
  return res

def oauth(speech_file_path = '../Documents/test_recording.flac'):
  import base64
  from apiclient.discovery import build
  from oauth2client import tools
  from oauth2client.file import Storage
  from oauth2client.client import AccessTokenRefreshError
  from oauth2client.client import OAuth2WebServerFlow

  with open('/users/smittapalli/.creds/gcloud_oauth','r') as credfile:
    OAUTH = credfile.readlines()
    OAUTH_CLIENT_ID = OAUTH[0][0:-1]
    OAUTH_SECRET = OAUTH[1][0:-1]

  scope = 'https://speech.googleapis.com/v1/speech:recognize'
  flow = OAuth2WebServerFlow(OAUTH_CLIENT_ID, OAUTH_SECRET, scope)

  storage = Storage('credentials.dat')
  credentials = storage.get()

  if credentials is None or credentials.invalid:
     credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

  # Create an httplib2.Http object to handle our HTTP requests, and authorize it
  # using the credentials.authorize() function.
  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('speech', 'v1', http=http)

  with open(speech_file_path, 'rb') as speech:
    speech_content = base64.b64encode(speech.read())

  request = service.speech().syncrecognize(
    body={ 'config': { 'languageCode': 'en-US', }, 'audio': { 'content': speech_content } })

  response = request.execute()

if __name__ == "__main__":
  pdb.set_trace()
