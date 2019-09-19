from flask import Flask, jsonify, request
import json

# The main Flask app
app = Flask(__name__)

# Data from a json file
data = json.load(open('coe332.json', 'r'))

@app.route('/')
def coe332():
    return jsonify(data)

@app.route('/instructors')
def get_instructors():
    return jsonify(data['instructors'])

@app.route('/instructors/<int:id>')
def get_instructors_by_id(id):
    if id >= len(data['instructors']):
        return '', 404
    return jsonify(data['instructors'][id])

@app.route('/assignments', methods=['GET'])
def get_assignments():
    return jsonify(data['assignments'])

@app.route('/assignments/<int:id>', methods=['GET'])
def get_assignments_by_id(id):
    if id >= len(data['assignments']):
        return '', 404
    return jsonify(data['assignments'][id])

@app.route('/assignments/<int:id>/<string:detail>', methods=['GET'])
def get_assignment_detail(id, detail):
    if id >= len(data['assignments']) or detail not in data['assignments'][id]:
        return '', 404
    return jsonify(data['assignments'][id][detail])

@app.route('/assignments', methods=['POST'])
def post_assignment():
    assignment = request.json
    data['assignments'].append(assignment)
    return '', 200

@app.route('/meeting')
def get_meeting():
    return jsonify(data['meeting'])

@app.route('/meeting/<string:detail>')
def get_meeting_key(detail):
    if detail not in data['meeting']:
        return '', 404
    return jsonify(data['meeting'][detail])

