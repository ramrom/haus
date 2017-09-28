# To run: FLASK_APP=homeserver.py flask run -p 1111 --host=1.1.1.1

import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def status():
  return 'hello world'

@app.route("/run")
def run():
  action = request.args.get('act','')
  if action == 'light':
    os.system('python ~/haus/haus.py light')
    return 'lights toggled'
  else:
    return 'unknown action'
