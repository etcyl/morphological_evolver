# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:05:42 2018

@author: etcyl
"""

class chromosome():
    
    def __init__(self, length):
        self.genes = [0]*length
        
    def toggle_gene(self, index):
        if(self.genes[index] == 0):
            self.genes[index] = 1
        else:
            self.genes[index] = 0
