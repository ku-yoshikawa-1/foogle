# if user.session!= null:
#     recommendation()
#
# else if user.session=null:
#     defaultranking()
#
#
#
#
#
# def food_ranking():
#
#     # get location of user
#
#
#     # compute distance of user and shops.
#
#
#     # list()
#
#
# def recommendation():
# of
#
# get(user.info).cordinate
# get(shop.info).cordinate
#
#
# get(food).shopname && price
#
# calculate(a,b,c)
# training_model()
# calculate(a,b,c)
# list(shops)
#
# return ...
#
# def getUserInfo(a,b,c):
#
#
#
# def getShopInfo(a,b,c):
#
#
#
#
# def dataProcess(a,b,c,):
#
#
#
#
#
# def distance(user, shop):
#
import numpy as np
from numpy import *
from numpy import genfromtxt
from sklearn.preprocessing import StandardScaler
from distance import *

from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import Adagrad
from keras.utils import to_categorical

# to get the history of users that he clicks food he likes
def get_trainingdata():
    train_data = genfromtxt('training_data.csv', delimiter=',')
    return train_data


# to get the food & user info so that we can train
def get_recommenddata():
    rec_data = genfromtxt('recommend.csv', delimiter=',')
    return rec_data


# get the training model of a user
def training():

# import data
    train_data = get_trainingdata()
    X = train_data[:, 0:6]
    y = train_data[:, 6]
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


def calculation():

    network = training()

    rec_data = get_recommenddata()
    index = rec_data[:,0]
    X_input = rec_data[:,1:]

    scaler = StandardScaler()
    scaler.fit(X_input)
    X_input = scaler.transform(X_input)

    y_pred_one_hot = network.predict(X_input)
    y_pred = np.argmax(y_pred_one_hot, axis=1)
    for i in range(len(X_input)):
        if y_pred[i]== 1:
            print(index[i])

    return index[i]


# def recommend():
#     user_info = standardization()
#     result = []
#     for x in user_info:
#         result.append([x[0], calculation(x[1], x[2], x[3])])
#
#     def take_second(elem):
#         return elem[1]
#     result.sort(key=take_second)
#     result = [i[0] for i in result]
#     print(result)

if __name__ == '__main__':
    calculation()
    # price=get_price()
    # distance=get_distance()
    # time=get_time()
    # calculation(price,location,time)
    # print("hello world!")




