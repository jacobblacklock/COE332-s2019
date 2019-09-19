from flask import Flask, jsonify, request
from redis import Redis, RedisError
import os
import socket
import requests
import json

# The main Flask app
app = Flask(__name__)

#Connecting to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

# Data from a json file
data = json.load(open('coe332.json', 'r'))

@app.route('/')
def coe332():
	return jsonify(data)

@app.route('/meeting')
def get_meeting():
	return jsonify(data['meeting'])

@app.route('/meeting/days')
def meeting_days():
	return jsonify(data['meeting']['days'])

@app.route('/instructors')
def get_instructors():
	return jsonify(data['instructors'])

@app.route('/instructors/<int:number>')
def instructor_number(number):
	return jsonify(data['instructors'][number])

@app.route('/assignments')
def get_assignments():
	return jsonify(data['assignments'])

@app.route('/assignments/<int:number>')
def assignment_number(number):
        return jsonify(data['assignments'][number])

@app.route('/assignments/<int:number>/url')
def assignment_url(number):
        return jsonify(data['assignments'][number]['url'])

@app.route('/assignments', methods=['POST'])
def post_assignment():
	response = request.data
	request_dictionary = json.loads(response)
	return jsonify(request_dictionary)
