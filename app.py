from flask import Flask, render_template, request
import twitter
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
#import plotly.plotly as py
from plotly.graph_objs import *


import plotly.graph_objs as go
from PIL import Image
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/index')
def index():
    lat = 60
    long = 30
    text = 'FLASK WORK'
    form = {'lat': lat, 'long': long}
    return render_template('index2.html', lat=lat, ln=long, text=text)

@app.route('/gpx_analyse')
def gpx_analyse():
	return render_template('gpx_analyse.html')
@app.route('/map_devices')
def map_devices():
	return render_template('map_devices.html')
@app.route('/plan')
def plan():
	return render_template('plan.html')
@app.route('/secure')
def secure():
	return render_template('secure.html')    
@app.route('/litter')
def litter():
    sum = 400
    posts = [
    {
        'author': {'username': 'Очень грязно'},
        'body': '72',
        'summ': '22',
        'color': 'green'
    },
    {
        'author': {'username': 'Грязно'},
        'body': '88',
        'summ': '23',
        'color': 'red'
    }, 
    {
        'author': {'username': 'Чисто'},
        'body': '334',
        'summ': '60',
        'color': 'aqua'
    }
    ]
    return render_template('litter2.html',  posts=posts, sum = sum) 
  
@app.route('/contact')
def contact():
	return render_template('contact.html') 

@app.route('/social')
def social():
    CONSUMER_KEY = 'u4SD5KlVGm59ftBTb69glEtp1'
    CONSUMER_SECRET = 'PCSFhTShUoKzASdExZh5pz54nP1v4uo0KheBotPpZUUoQ3r1sV'
    OAUTH_TOKEN = '2308267840-G9kog927ZlVhGvoUsXbIt16ZQLk0eUkeuteieA6'
    OAUTH_TOKEN_SECRET = '6ZW7GNAZTG6tW4YXYShawMgGbv5ri4kfZvgDF1UAbSb4a'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    tweet=twitter_api.search.tweets(q='Сосновый бор')
    p = json.dumps(tweet)
    res2 = json.loads(p)
    j=0
    post=[]
    while j<len(res2['statuses']):
        dict1={'author': {'username': (res2['statuses'][j]['user']['name'])},
            'body': res2['statuses'][j]['text'],
               'date':res2['statuses'][j]['created_at'],
               'lang': res2['statuses'][j]['user']['lang'],
               'count': res2['statuses'][j]['user']['followers_count'],
               'status': res2['statuses'][j]['user']['statuses_count']}
        post.append(dict1)
        j=j+1
    return render_template('social_true.html', title='Home', posts=post)
if __name__ == '__main__':
	app.run(debug=True)
