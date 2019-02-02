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
    with open('show_data.json') as f:
        data = json.load(f)
    return jsonify(data);

