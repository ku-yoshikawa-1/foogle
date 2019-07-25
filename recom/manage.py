
import numpy as np
from numpy import *
from numpy import genfromtxt
from sklearn.preprocessing import StandardScaler
from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import Adagrad
from keras.utils import to_categorical
import pymysql
from math import radians, cos, sin, asin, sqrt
import sys

all_info = []
# id,product_name,shop_name,price,end_time,latitude,longitude

# connect with mysql
def get_conn():
    conn = pymysql.connect(host='mysql', port=3306, user='root', passwd='admin', db='db')    # db:表示数据库名称
    return conn


# execute the query
def query(sql, args):
    all_info.clear()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    for row in results:
        id = row[0]
        product_name=row[1]
        shop_name=row[2]
        price= row[3]
        end_time=row[4]
        latitude = row[5]
        longitude = row[6]
        all_info.append([id,product_name,shop_name,price,end_time,latitude,longitude])
        pass
    conn.commit()
    cur.close()
    conn.close()


# give query sentence
def get_allinfo(product_name):
    search = product_name
    a = '\'' + search + '\''
    sql = 'SELECT id, product_name, bargain_info.shop_name, price, end_time, latitude, longitude FROM shop_info, bargain_info WHERE shop_info.shop_name=bargain_info.shop_name AND product_name=' + a + ';'
    query(sql, None)


# We use a fake function, which should be located by Google API
def get_userloc():
    # user_loc gets by GeoAPI, there we use a static one for Demonstration
    user_loc = (35.0268, 135.7796)
    return user_loc


# get shop location
def get_shoploc():
    shop_loc = []
    for item in all_info:
        shop_loc.append([item[5], item[6]])
    return shop_loc


# compute distance of two point
def haversine(user_loc, shop_loc):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lat1 = user_loc[0]
    lat2 = shop_loc[0]
    lon1 = user_loc[1]
    lon2 = shop_loc[1]
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


# get distance between use and all shops which has the food he wants
def get_distance():
    user_loc=get_userloc()
    shop_loc=get_shoploc()
    distance = []
    for i in range(len(shop_loc)):
        distance.append(haversine(user_loc, shop_loc[i]))
    return distance


# input the data, which is from database
def get_recommenddata():
    distance=get_distance()
    rec_data=[]
    for i in range(len(all_info)):
        rec_data.append([all_info[i][0], all_info[i][3], distance[i], 10])
    rec_data = array(rec_data)
    return rec_data


# input the training data, which is static csv file
def get_trainingdata():
    train_data = genfromtxt('/root/recom/training_data.csv', delimiter=',')
    return train_data

# get the training model of a user
def training():

# import data
    train_data = get_trainingdata()
    X = train_data[:, 0:3]
    y = train_data[:, 3]
    number_samples = X.shape[0]
    training_ratio = 0.8
    train_samples = int(training_ratio * number_samples)
    X_train = X[:train_samples]
    y_train = y[:train_samples]
    X_test = X[train_samples:]
    y_test = y[train_samples:]


# standarization
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)


# model neural network
    input_shape = X_train[0].shape
    vector_input = Input(shape=input_shape, name='input')
    fc1 = Dense(10, activation='tanh', name='fc1')(vector_input)
    fc2 = Dense(10, activation='tanh', name='fc2')(fc1)
    output = Dense(2, activation='softmax', name='output')(fc2)
    network = Model(vector_input, output, name='classification')
    network.compile(loss='categorical_crossentropy', optimizer=Adagrad(lr=0.01), metrics=['acc'])
    y_train_one_hot = to_categorical(y_train)
    y_test_one_hot = to_categorical(y_test)
    H = network.fit(X_train, y_train_one_hot, batch_size=10, epochs=50, validation_data=(X_test, y_test_one_hot))
    # y_pred_one_hot = network.predict(X_test)
    # y_pred = np.argmax(y_pred_one_hot, axis=1)
    return network


def recommend():

    network = training()

    rec_data = get_recommenddata()
    index = rec_data[:,0]
    X_input = rec_data[:,1:]

    scaler = StandardScaler()
    scaler.fit(X_input)
    X_input = scaler.transform(X_input)

    y_pred_one_hot = network.predict(X_input)
    y_pred = np.argmax(y_pred_one_hot, axis=1)
    bargain_ids=[]
    for i in range(len(X_input)):
        if y_pred[i]== 1:
            bargain_ids.append(int(index[i]))

    return bargain_ids

def main(product_name):
    get_allinfo(product_name)
    bargain_ids = recommend()
    return bargain_ids

#  this is main function. you need to input this argument.  use API



