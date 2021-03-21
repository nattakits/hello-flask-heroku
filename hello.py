from flask import Flask
from flask_jsonpify import jsonpify
from flask_restful import Resource,Api,reqparse
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!!!'

if __name__ == '__main__':
    app.run()
