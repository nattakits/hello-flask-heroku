from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
import json
from tweepy import OAuthHandler
from tweepy import API
import tweepy

app = Flask(__name__)
Bootstrap(app)




Hastag=['dfg']
Volumns=['dfg']
Order=['dg']
Url=['dfgdf']


@app.route('/')
def index():
    return render_template('index.html',Hastag=Hastag,Volumns=Volumns,Order=Order,Url=Url)

if __name__ == '__main__':
    app.run(debug=True)
