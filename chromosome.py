# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:05:42 2018

@author: etcyl
"""

import random

class chromosome():
    
    def __init__(self, length):
        self.genes = [0]*length
        for i in range(length):
            if(random.randint(0, 1) == 1):
                self.setGene(i, 1)
            else:
                self.setGene(i, 0)
        
    def toggleGene(self, index):
        if(self.genes[index] == 0):
            self.genes[index] = 1
        else:
            self.genes[index] = 0
            
    def getGene(self, index):
        return self.genes[index]
    
    def setGene(self, index, value):
        self.genes[index] = value
