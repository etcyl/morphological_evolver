# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:56:29 2018

@author: Etcyl
"""

from keras.datasets import cifar10
import cv2
import numpy as np

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

imageB = x_train[0]
kernel = np.ones((2,2),np.uint8)
#er = cv2.erode(imageB,kernel,iterations = 1)

while True:
    cv2.imshow("Image", imageB)
    key = cv2.waitKey(1) & 0xFF
    
    if key==ord("q"): # if the user presses "q" while looking at the canvas, then quit
        break
        
print("Closing all active windows")
cv2.destroyAllWindows()
