#!/usr/local/bin/python
# script from: https://stackoverflow.com/questions/38703853/how-to-use-google-speech-recognition-api-in-python

import pdb
#import subprocess
#task = subprocess.Popen("cat file.log | tail -1", shell=True, stdout=subprocess.PIPE)
#data = task.stdout.read()

with open('/users/smittapalli/.creds/gcloud_oauth','r') as credfile:
  OAUTH = credfile.readlines()
  OAUTH_CLIENT_ID = OAUTH[0][0:-1]
  OAUTH_SECRET = OAUTH[1][0:-1]

#pdb.set_trace()

DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

def get_speech_service():
  from oauth2client.client import GoogleCredentials

  credentials = GoogleCredentials.get_application_default().create_scoped(
      ['https://www.googleapis.com/auth/cloud-platform'])
  http = httplib2.Http()
  credentials.authorize(http)
  return discovery.build('speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)

def methodA(speech_file):
  import base64
  import json
  import httplib2

  from googleapiclient import discovery

  with open(speech_file, 'rb') as speech:
    speech_content = base64.b64encode(speech.read())

  service = get_speech_service()
  service_request = service.speech().syncrecognize(
    body={
      'config': {
        'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
        'sampleRate': 16000,  # 16 khz
        'languageCode': 'en-US',  # a BCP-47 language tag
      },
    'audio': {
      'content': speech_content.decode('UTF-8')
      }
    })
  response = service_request.execute()
  print(json.dumps(response))

def methodB():
  from apiclient.discovery import build
  from oauth2client import tools
  from oauth2client.file import Storage
  from oauth2client.client import AccessTokenRefreshError
  from oauth2client.client import OAuth2WebServerFlow

  scope = 'https://www.googleapis.com/auth/calendar'
  flow = OAuth2WebServerFlow(client_id, client_secret, scope)

  storage = Storage('credentials.dat')
  credentials = storage.get()

  if credentials is None or credentials.invalid:
     credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

  # Create an httplib2.Http object to handle our HTTP requests, and authorize it
  # using the credentials.authorize() function.
  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('calendar', 'v3', http=http)

  try:
    request = service.events().list(calendarId='primary')

    while request != None:
    response = request.execute()

    for event in response.get('items', []):
      # The event object is a dict object with a 'summary' key.
      print repr(event.get('summary', 'NO SUMMARY')) + '\n'
    # Get the next request object by passing the previous request object to
    # the list_next method.
    request = service.events().list_next(request, response)

  except AccessTokenRefreshError:
    # The AccessTokenRefreshError exception is raised if the credentials
    # have been revoked by the user or they have expired.
    print ('The credentials have been revoked or expired, please re-run' 'the application to re-authorize')


if __name__ == "__main__":
  print "usage: 1 to print long/lat"
  #if len(sys.argv) > 1 and sys.argv[1] == '1':
  pdb.set_trace()
