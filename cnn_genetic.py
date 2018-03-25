# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 07:27:22 2018

Uses a genetic algorthim to evolve a combination of morphological operators to apply the CIFAR-10
dataset as a function of a CNN's accuracy (trained on the morphed data).

@author: Etcyl
"""

import build_cnn
import genetic
import keras
from keras.datasets import cifar10

batch_size = 32
num_classes = 10
epochs = 1#100
data_augmentation = True
num_predictions = 20

#Get the CIFAR-10 data and training sets
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

evolver = genetic.morphological_evolver()

for i in range(len(evolver.pop_size)):
    cnn = build_cnn.buildCNN()
