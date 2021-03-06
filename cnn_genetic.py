# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 07:27:22 2018

Uses a genetic algorthim to evolve a combination of morphological operators to apply the CIFAR-10
dataset as a function of a CNN's accuracy (trained on the morphed data).

@author: Etcyl
"""

from keras.datasets import cifar10
import build_cnn
import genetic
import keras
import cv2
import numpy as np

#Set constants here
batch_size = 32
num_classes = 10
epochs = 1#100
data_augmentation = True
num_predictions = 20
kernel = np.ones((3,3),np.uint8)

#Create a genetic algorithm class to use the genetic algorithm
evolver = genetic.morphological_evolver()

for k in range(evolver.generations):
    #Use each chromosome in the population to train the CNN
    for index in range(evolver.pop_size):
        #Get the CIFAR-10 data and training sets
        (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        #Convert class vectors to binary class matrices
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)
        
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255

        #Create the CNN class using Keras
        cnn = build_cnn.buildCNN()
        
        if(k == 0): #Update every individual for the first generation, k == 0, and then only the children after
            #If a gene is present, decode and apply it to the dataset before training the CNN
            for j in range(evolver.num_genes):
                if evolver.current_pop[index].getGene(j) == 1:
                    if j == 1: #Erosion
                        for i in range(len(x_train)):
                            x_train[i] = cv2.erode(x_train[i], kernel, iterations = 1)
                        for i in range(len(x_test)):
                            x_test[i] = cv2.erode(x_test[i], kernel, iterations = 1)
                    elif j == 2: #Dilation
                        for i in range(len(x_train)):
                            x_train[i] = cv2.dilate(x_train[i], kernel, iterations = 1)
                        for i in range(len(x_test)):
                            x_test[i] = cv2.dilate(x_test[i], kernel, iterations = 1)
                    elif j == 3: #Opening
                        for i in range(len(x_train)):
                            x_train[i] = cv2.morphologyEx(x_train[i], cv2.MORPH_OPEN, kernel)
                        for i in range(len(x_test)):
                            x_test[i] = cv2.morphologyEx(x_test[i], cv2.MORPH_OPEN, kernel)
                    elif j == 4: #Closing
                        for i in range(len(x_train)):
                            x_train[i] = cv2.morphologyEx(x_train[i], cv2.MORPH_CLOSE, kernel)
                        for i in range(len(x_test)):
                            x_test[i] = cv2.morphologyEx(x_test[i], cv2.MORPH_CLOSE, kernel)
                    elif j == 5: #Gradient
                        for i in range(len(x_train)):
                            x_train[i] = cv2.morphologyEx(x_train[i], cv2.MORPH_GRADIENT, kernel)
                        for i in range(len(x_test)):
                            x_test[i] = cv2.morphologyEx(x_test[i], cv2.MORPH_GRADIENT, kernel)
            cnn.fit(x_train[0:1000], y_train[0:1000], batch_size=batch_size, epochs=epochs,
                  validation_data=(x_test[0:1000], y_test[0:1000]), shuffle=True)
            scores = cnn.evaluate(x_test[0:1000], y_test[0:1000], verbose=1)
            #print('Test loss:', scores[0])
            print('Test accuracy:', scores[1])
            evolver.current_pop[index].setAccuracy(scores[1])
                            
        elif(k > 0): #First generation is complete, so only update for future children
            if(evolver.current_pop[index].getAccuracy() == 0): #Find children by getting individuals that have 0 accuracy 
                for j in range(evolver.num_genes):
                    if evolver.current_pop[index].getGene(j) == 1:
                        if j == 0: #Erosion
                            for i in range(len(x_train)):
                                x_train[i] = cv2.erode(x_train[i], kernel, iterations = 1)
                            for i in range(len(x_test)):
                                x_test[i] = cv2.erode(x_test[i], kernel, iterations = 1)
                        elif j == 1: #Dilation
                            for i in range(len(x_train)):
                                x_train[i] = cv2.dilate(x_train[i], kernel, iterations = 1)
                            for i in range(len(x_test)):
                                x_test[i] = cv2.dilate(x_test[i], kernel, iterations = 1)
                        elif j == 2: #Opening
                            for i in range(len(x_train)):
                                x_train[i] = cv2.morphologyEx(x_train[i], cv2.MORPH_OPEN, kernel)
                            for i in range(len(x_test)):
                                x_test[i] = cv2.morphologyEx(x_test[i], cv2.MORPH_OPEN, kernel)
                        elif j == 3: #Closing
                            for i in range(len(x_train)):
                                x_train[i] = cv2.morphologyEx(x_train[i], cv2.MORPH_CLOSE, kernel)
                            for i in range(len(x_test)):
                                x_test[i] = cv2.morphologyEx(x_test[i], cv2.MORPH_CLOSE, kernel)
                        elif j == 4: #Gradient
                            for i in range(len(x_train)):
                                x_train[i] = cv2.morphologyEx(x_train[i], cv2.MORPH_GRADIENT, kernel)
                            for i in range(len(x_test)):
                                x_test[i] = cv2.morphologyEx(x_test[i], cv2.MORPH_GRADIENT, kernel)
                cnn.fit(x_train[0:1000], y_train[0:1000], batch_size=batch_size, epochs=epochs,
                  validation_data=(x_test[0:1000], y_test[0:1000]), shuffle=True)
                scores = cnn.evaluate(x_test[0:1000], y_test[0:1000], verbose=1)
                #print('Test loss:', scores[0])
                print('Test accuracy:', scores[1])
                evolver.current_pop[index].setAccuracy(scores[1])
                
    evolver.updatePop() #Create a new generation using crossover and mutation
