from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)
conn = mysql.connect()


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