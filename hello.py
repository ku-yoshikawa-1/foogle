from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE'] = 'db'

mysql = MySQL(app)


@app.route('/')
def index():
    return jsonify({
      'test': 'Hello, API'
    })

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT product_id FROM db.bargain_info''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/hello')
def hello():
    return jsonify({
      'test': 'Hello, API2'
    })

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')