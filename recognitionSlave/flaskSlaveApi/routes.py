from flask import render_template, request, jsonify
from recognitionSlave.flaskSlaveApi import app
import sys



@app.route('/')
@app.route('/home')
def home():
    return "slave home port " + sys.argv[1]