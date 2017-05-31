#!/usr/local/bin/python
import pdb
#import google-api-python-client
from apiclient.discovery import build

#import subprocess
#task = subprocess.Popen("cat file.log | tail -1", shell=True, stdout=subprocess.PIPE)
#data = task.stdout.read()

f = open('/users/smittapalli/.creds/gcloud_oauth','r')
OAUTH = f.readlines()
OAUTH_CLIENT_ID = OAUTH[0][0:-1]
OAUTH_SECRET = OAUTH[1][0:-1]
f.close()

pdb.set_trace()

def g_sp_recog():
  print 'hi'
