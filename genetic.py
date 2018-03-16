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
        num_generations:    Number of generations, or number of times to evolve the chromosomes;
                             if this is not set, the default value is 100.
        population_size:    Number of chromosomes/individuals in the population for each generation;
                             if this is not set, the default value is 4.
        baseline_accuracy:  Standard to evolve towards, i.e. the accuracy that is ideally achieved
                             after evolving the network num_generations times;
                             if this is not set, the default value is 75%
    """
    
    def __init__(self, num_generations = None, population_size = None, baseline_accuracy = None):
        if num_generations is None:
            self.generations = 100
        else:
            self.generations = num_generations 
        if population_size is None:
            self.pop_size = 4
        else:
            self.pop_size = population_size
        if baseline_accuracy is None:
            self.base_accuracy = 0.75
        else:
            self.base_accuracy = baseline_accuracy
        self.num_operators = 7 #Number of morphological operators, or genes 
        self.current_accuracy = 0 #Current accuracy of the SVM using the applied morpholigcal operators
        self.current_chromosome = [0]*self.num_operators #List to keep track of the current most fit chromosome
        
    def getAccuracy(self):
        return self.current_accuracy
    
    def getChromosome(self):
        return self.current_chromosome
    
    def setAccuracy(self, accuracy):
        self.current_accuracy = accuracy
        
    def setChromosome(self, chromosome):
        self.current_chromosome = chromosome
    
    def evaluateFitness(self, accuracy):
       if(accuracy == self.base_accuracy):
           return 1
       else:
           return 0
       
    def mutateParents(self, parentA, parentB):
        childA = [0]*self.num_operators
        childB = [0]*self.num_operators
        for i in range(3): 
            #Crossover point is the 4th element in the list
            #Take parentB's first 3 elements and replace parentA's first 3 elements with them
            #Take parentA's first 3 elements and replace parentB's first 3 elements with them
            childA[i] = parentB[i]
            childA[i + 3] = parentA[i + 3]
            childB[i] = parentA[i]
            childB[i + 3] = parentB[i + 3]
        childA[-1] = parentA[-1]
        childB[-1] = parentB[-1]
        return (childA, childB)
