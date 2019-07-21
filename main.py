from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from recommend import recommend
import sys

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

@app.route('/my_profile')
def my_profile():
  cur = mysql.connection.cursor()
  cur.execute('''SELECT user_id, first_name, last_name FROM db.user''')
  rv = cur.fetchall()
  col = ('user_id', 'first_name', 'last_name')
  return jsonify(dict(zip(col, rv)))

@app.route('/shops/<shop_name>')
def shop(shop_name=None):
  cur = mysql.connection.cursor()
  cur.execute('''SELECT * FROM db.shop_info
    WHERE shop_name = \'%s\'''' % (shop_name))
  rv = cur.fetchall()[0]
  col = ('shop_id', 'shop_name', 'latitude', 'longitude', 'brand', 'shop_description')
  return jsonify(dict(zip(col, rv)))

@app.route('/products/<product_name>')
def product(product_name=None):
  cur = mysql.connection.cursor()
  cur.execute('''SELECT * FROM db.product_info
    WHERE product_name = \'%s\'''' % (product_name))
  rv = cur.fetchall()
  col = ('product_id', 'product_name', 'category_name', 'type', 'pna1', 'pna2', 'pna3', 'cna1', 'cna2', 'cna3')
  return jsonify(dict(zip(col, rv)))

@app.route('/bargain')
def bargain():
  product = request.args.get('product')
  shop = request.args.get('shop')
  cur = mysql.connection.cursor()
  query = ''
  if product and shop:
    query = '''SELECT * FROM db.bargain_info WHERE product_name = \'%s\' AND shop_name = \'%s\' ''' % (product, shop)
  elif product:
    query = '''SELECT * FROM db.bargain_info WHERE product_name = \'%s\'''' % (product)
  elif shop:
    query = '''SELECT * FROM db.bargain_info WHERE shop_name = \'%s\' ''' % (shop)

  cur.execute(query)
  rv = cur.fetchall()
  col = ('id', 'product_name', 'shop_name', 'price', 'end_time', 'price_peritem', 'pack_ll', 'pack_ul', 'pack_size', 'item_size', 'pack_type')
  print('ok', file=sys.stderr)
  return jsonify(list(map(lambda x: dict(zip(col, x)), rv)))

@app.route('/search')
def search():
  products = request.args.get('products')
  shops = request.args.get('product')
  return recommend(products, shops)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')