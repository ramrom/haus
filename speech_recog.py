#!/usr/local/bin/python
import pdb
#import google-api-python-client
from apiclient.discovery import build

#import subprocess
#task = subprocess.Popen("cat file.log | tail -1", shell=True, stdout=subprocess.PIPE)
#data = task.stdout.read()

with open('/users/smittapalli/.creds/gcloud_oauth','r') as credfile:
  OAUTH = credfile.readlines()
  OAUTH_CLIENT_ID = OAUTH[0][0:-1]
  OAUTH_SECRET = OAUTH[1][0:-1]

#pdb.set_trace()

import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


def get_speech_service():
  credentials = GoogleCredentials.get_application_default().create_scoped(
      ['https://www.googleapis.com/auth/cloud-platform'])
  http = httplib2.Http()
  credentials.authorize(http)
  return discovery.build('speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def main(speech_file):
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
