#!/usr/bin/env python

import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world_page():
	r = requests.get('http://hello-world-back:5000/getmessage')
	return '<html><body><h1>'+r.text+'</h1></body></html>'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
