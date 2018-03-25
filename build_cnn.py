# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 07:34:00 2018

Builds and returns a CNN using the Keras API following the original source: 
    https://github.com/keras-team/keras/blob/master/examples/cifar10_cnn.py

@author: Etcyl
"""

import keras
from keras import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

shape = (32, 32, 3) #x_train.shape[1:], where x_train is from the CIFAR-10 dataset
num_classes = 10

def buildCNN():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=shape))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    # initiate RMSprop optimizer
    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

    # Let's train the model using RMSprop
    model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])
    return model
