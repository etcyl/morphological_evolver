# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:42:05 2018
Matt Fleetwood
ECE 479/579 - Intelligent Robotics II
Winter 2018

Genetic algorithm that evolves a string of morphological operators and a structuring element.
The morpholigcal operators are stored in a list and applied sequentially, e.g. the 0th 
operator is applied first to a CIFAR-10 dataset image, then the 1st, etc.
A Support Vector Machine (SVM) is trained on the modified images.
The classification accuracy is compared with a reference SVM, an SVM trained on the non-modified 
dataset. The "most fit" string of operators and structuring element are evolved until the 
SVM using them achieves accuracy as good or better than the reference SVM.

@author: etcyl
"""

class morphological_evolver():
    """The morphoglogical_evolver evolves a list of morphological operators"""
    #The class creates new chromosomes, lists of m_operators, from genes (m_operators)
    
    type = 'Crossover mutation for SVM training on the CIFAR-10 dataset'
    
    """
    Init / constructor arguments: 
        num_generations: Number of generations, or number of times to evolve the chromosomes;
                         if this is not set, the default value is 100.
        population_size: Number of chromosomes/individuals in the population for each generation;
                         if this is not set, the default value is 4.
    """
    
    def __init__(self, num_generations = None, population_size = None):
        if num_generations is None:
            self.generations = 100
        else:
            self.generations = num_generations 
        if population_size is None:
            self.pop_size = 4
        else:
            self.pop_size = population_size
        self.current_accuracy = 0 #Current accuracy of the SVM using the applied morpholigcal operators
        self.current_chromosome = [] #List to keep track of the current most fit chromosome
        
    def getAccuracy(self):
        return self.current_accuracy
    
    def getChromosome(self):
        return self.current_chromosome
