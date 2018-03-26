# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:05:42 2018

Chromosomes are a list of genes, in this case each element in the list represents a morphologial operator:
    
    0: No operator
    1: Erosion
    2: Dilation (opposite of erosion)
    3: Opening (erosion followed by dilation)
    4: Closing (dilation followed by erosion)
    5: Gradient (difference between dilation and erosion of an image)
    5: Thinning <--- not yet implemented
    6: Thickening <--- not yet implemented

@author: etcyl
"""

import random

class chromosome():
    
    def __init__(self, length):
        self.accuracy = 0#random.randint(0, 99) #Accuracy of an SVM, when it sequentially applies the genes to an image
        self.genes = [0]*length #Storage for an individual
        for i in range(length): #For all the genes in the list, 50% for the current element to be present or absent
            if(random.randint(0, 1) == 1):
                self.setGene(i, random.randint(1, 5)) #Random value was 1 so the gene is present
            else:
                self.setGene(i, 0) #Random value was 0 so the gene is absent
        
    def toggleGene(self, index): #Turn the gene on or off
            self.genes[index] = 0
            
    def getGene(self, index):
        return self.genes[index]
    
    def setGene(self, index, value):
        self.genes[index] = value
        
    def getAccuracy(self):
        return self.accuracy
    
    def setAccuracy(self, new_accuracy):
        self.accuracy = new_accuracy
    
    def getChromosome(self):
        return self.genes
    
    def setChromosome(self, genes):
        self.genes = genes
