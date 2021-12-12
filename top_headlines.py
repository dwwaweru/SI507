#flaskapphelloname.py
from flask import Flask, render_template
import requests
from secret import *
import json



app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)       

def getarticles():
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key="
    key = api_key
    response = requests.get(base_url+key)
    result = response.json()
    return result

@app.route('/headlines/<nm>')
def headlines(nm):
    articles = getarticles()['results'][:5]
    li_headlines = [articles[i]['title'] for i in range(len(articles))]
    return render_template('headlines.html', headlines=li_headlines, name=nm)

@app.route('/links/<nm>')
def links(nm):
    #li_headlines = ["t1", "t2", "t3"]
    articles = getarticles()['results'][:5]
    # print(articles)
    info = [(articles[i]['title'], articles[i]['url'])  for i in range(len(articles))]
    return render_template('links.html', information=info, name=nm)       

if __name__ == '__main__':  
    app.run(debug=True)

