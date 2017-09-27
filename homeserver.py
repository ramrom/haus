# To run: FLASK_APP=homeserver.py flask run -p 8080 --host=192.168.1.102

from flask import Flask
app = Flask(__name__)

@app.route("/")
def run():
  return 'hello world'
