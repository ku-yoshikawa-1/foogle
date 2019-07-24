from sqlalchemy import create_engine
import pymysql


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='db')    # db:表示数据库名称
    return conn


def query(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    query_result=[]
    for row in results:
        id = row[0]
        latitude = row[1]
        longitude = row[2]
        print(id)
        pass

    conn.commit()
    cur.close()
    conn.close()
    return query_result


if __name__ == '__main__':
    search = 'ほうれん草'
    a = '\'' + search + '\''
    sql = 'SELECT id, latitude, longitude FROM shop_info, bargain_info WHERE shop_info.shop_name=bargain_info.shop_name AND product_name=' + a +';'
    query(sql, None)

