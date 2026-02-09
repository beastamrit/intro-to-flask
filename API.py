from flask import Flask,render_template
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def details():
    location = input("Enter the location here:")
    api_key ='AQw4sN0X1A9KQf6l5TtN_2GgSrgc63hY04_h8ps'

    try:
        source= urllib.request.urlopen(https://geocode.search.hereapi.com/v1/geocode?apikeys=%27+api_key+%27&q=%27+location).read()