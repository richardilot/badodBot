#web framework for python
#quickstart documentation https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart
#this code is inspired from (Discord) M692#4523

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Webserver UP, Discord Bot UP"

def run():
  app.run(host='0.0.0.0', port=8080)  

def keep_alive():
  t = Thread(target=run)
  t.start()