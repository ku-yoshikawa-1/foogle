from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({
      'test': 'Hello, API'
    })

@app.route('/hello')
def hello():
    return jsonify({
      'test': 'Hello, API2'
    })

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')