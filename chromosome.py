# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:05:42 2018

@author: etcyl
"""

import random

class chromosome():
    
    def __init__(self, length):
        self.accuruacy = 0 #Accuracy of an SVM, when it sequentially applies the genes to an image
        self.genes = [0]*length #Storage for an individual
        for i in range(length): #For all the genes in the list, 50% for the current element to be present or absent
            if(random.randint(0, 1) == 1):
                self.setGene(i, 1) #Random value was 1 so the gene is present
            else:
                self.setGene(i, 0) #Random value was 0 so the gene is absent
        
    def toggleGene(self, index): #Turn the gene on or off, depending on the previous state (present or absent)
        if(self.genes[index] == 0):
            self.genes[index] = 1
        else:
            self.genes[index] = 0
            
    def getGene(self, index):
        return self.genes[index]
    
    def setGene(self, index, value):
        self.genes[index] = value
