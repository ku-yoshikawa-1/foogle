from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from recommend import recommend
from recom import manage
import sys

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE'] = 'db'
app.config['JSON_AS_ASCII'] = False

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

@app.route('/shops')
def shop():
  shop_name = request.args.get('shop')
  cur = mysql.connection.cursor()
  cur.execute('''SELECT * FROM db.shop_info
    WHERE shop_name = \'%s\'''' % (shop_name))
  rv = cur.fetchall()[0]
  col = ('shop_id', 'shop_name', 'latitude', 'longitude', 'brand', 'shop_description', 'url', 'photo')
  return jsonify(dict(zip(col, rv)))

@app.route('/products')
def product():
  product_name = request.args.get('product')
  cur = mysql.connection.cursor()
  cur.execute('''SELECT * FROM db.product_info
    WHERE product_name = \'%s\'''' % (product_name))
  rv = cur.fetchall()[0]
  col = ('product_id', 'product_name', 'category_name', 'type', 'pna1', 'pna2', 'pna3', 'cna1', 'cna2', 'cna3')
  return jsonify(dict(zip(col, rv)))

@app.route('/bargains')
def bargain():
  product = request.args.get('product')
  shop = request.args.get('shop')
  if not product:
    query = '''SELECT * FROM db.bargain_info WHERE shop_name = \'%s\' ''' % (shop)
    cur = mysql.connection.cursor()
    cur.execute(query)
    rv = cur.fetchall()
    response = []
    for row in rv:
      shop_name = row[2]
      cur.execute('''SELECT * FROM db.shop_info
          WHERE shop_name = \'%s\'''' % (shop_name))
      shop_rv = cur.fetchall()[0]
      shop_info = tuple([shop_rv[2], shop_rv[3], shop_rv[6], shop_rv[7]])
      response.append(row + shop_info)

    col = ('id', 'product_name', 'shop_name', 'price', 'end_time', 'price_peritem', 'pack_ll', 'pack_ul', 'pack_size', \
        'item_size', 'pack_type', 'latitude', 'longitude', 'shop_url', 'shop_img')
  
    return jsonify(list(map(lambda x: dict(zip(col, x)), response)))
    
  bargain_ids = manage.main(product)
  cur = mysql.connection.cursor()
  print(type(bargain_ids), file=sys.stderr)
  values = ', '.join(list(map(lambda x: str(x), bargain_ids)))
  query = "SELECT * FROM db.bargain_info WHERE id IN (%s)" % (values)
  cur.execute(query)
  rv = cur.fetchall()
  response = []
  for row in rv:
    shop_name = row[2]
    cur.execute('''SELECT * FROM db.shop_info
        WHERE shop_name = \'%s\'''' % (shop_name))
    shop_rv = cur.fetchall()[0]
    shop_info = tuple([shop_rv[2], shop_rv[3], shop_rv[6], shop_rv[7]])
    response.append(row + shop_info)
  col = ('id', 'product_name', 'shop_name', 'price', 'end_time', 'price_peritem', 'pack_ll', 'pack_ul', 'pack_size', \
         'item_size', 'pack_type', 'latitude', 'longitude', 'shop_url', 'shop_img')
  
  return jsonify(list(map(lambda x: dict(zip(col, x)), response)))

@app.route('/search')
def search():
  products = request.args.get('products').split(',') if request.args.get('products') else ()
  shops = request.args.get('shops').split(',') if request.args.get('shops') else ()
  return recommend(products, shops, mysql)

@app.route('/like')
def like():
  bargain = request.args.get('bargain_id')
  return 'ok'

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
