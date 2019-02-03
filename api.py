from flask import Flask
from flask import jsonify
import json
from pprint import pprint
app = Flask(__name__)

@app.route('/')
def index():
    return 'This API is for the CBCRAHackathon - Team PaypalGang'

@app.route("/shows/<userId>")
def get_shows(userId):

    user_keywords = get_user_keywords(userId)
    print(user_keywords)

    with open('show_data.json') as f:
        data = json.load(f)

        for d in data:
            show_keywords = get_show_keywords(d["description"])
            d["image"] = get_show_image(show_keywords, user_keywords)

    return jsonify(data)

def get_user_keywords(userId):
    return "technology"

def get_show_keywords(description):
    return "canada"

def get_show_image(showKeywords, userKeywords):
    return "https://www.cbc.ca/radio/podcasts/images/950x950/the180-podcast-template.jpg"