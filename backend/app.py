from flask import Flask, jsonify, request

app = Flask(__name__)

@app.after_request
def cors_headers(whatever):
    whatever.headers['Access-Control-Allow-Origin'] = '*'
    return whatever

@app.route('/api/hello', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hi from Flask'})