from flask import jsonify
import sys

def _querize(tup):
  print(type(tup), file=sys.stderr)
  return ','.join(list(map(lambda x: '"%s"' % x, tup)))

def recommend(products, shops, mysql):
  # TO_DO: replace to recommendation
  cur = mysql.connection.cursor()
  if products and shops:
    query = '''SELECT * FROM db.bargain_info WHERE product_name IN (%s) AND shop_name IN (%s)''' % (_querize(products), _querize(shops))
  elif products:
    query = '''SELECT * FROM db.bargain_info WHERE product_name IN (%s)''' % (_querize(products))
  elif shops:
    query = '''SELECT * FROM db.bargain_info WHERE shop_name IN (%s)''' % (_querize(shops))
  else:
    query = '''SELECT * FROM db.bargain_info'''
  cur.execute(query)
  rv = cur.fetchall()
  col = ('id', 'product_name', 'shop_name', 'price', 'end_time', 'price_peritem', 'pack_ll', 'pack_ul', 'pack_size', 'item_size', 'pack_type')

  return jsonify(list(map(lambda x: dict(zip(col, x)), rv)))