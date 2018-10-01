#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/getmessage')
def hello_world():
	return 'Hello Docker World!'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
