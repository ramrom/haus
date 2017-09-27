# To run: FLASK_APP=homeserver.py flask run -p 8080 --host=192.168.1.102

import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def run():
  action = request.args.get('act','')
  os.system('python ~/haus/haus.py light')
  return 'hello world'
