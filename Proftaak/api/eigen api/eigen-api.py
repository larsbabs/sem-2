import flask
import os
from flask import request, jsonify
from app import app, mongo
import logger

app = flask.Flask(__name__)
app.config["DEBUG"] = True
books = open("./books.json")

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/groep1/opdracht1/', methods=['GET', 'POST'])
def babs():
    if request.method == 'GET':
        return ""
    if request.method == 'POST':
        test = request.form["babs"]
    return books.read()
@app.route('/babs/', methods=['GET'])
def test():
    return "<h1>babs</h1>"

app.run(host="0.0.0.0")