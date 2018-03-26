# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:42:05 2018
Matt Fleetwood
ECE 479/579 - Intelligent Robotics II
Winter 2018

Genetic algorithm that evolves a string of morphological operators.
The morpholigcal operators are stored in a list and applied sequentially, e.g. the 0th 
operator is applied first to a CIFAR-10 dataset image, then the 1st, etc.
A Convolutional Neural Network (CNN) is trained on the modified images.
The classification accuracy is compared with a reference CNN, a CNN trained on the non-modified 
dataset. The "most fit" string of operators are evolved until the CNN using them achieves 
accuracy as good or better than the reference CNN.

@author: etcyl
"""

import random
import chromosome as ch

class morphological_evolver():
    """The morphoglogical_evolver evolves a list of morphological operators"""
    #The class creates new chromosomes, lists of m_operators, from genes (m_operators)
    
    type = 'Crossover mutation for CNN training on the CIFAR-10 dataset'
    
    """
    Init / constructor arguments: 
        num_generations:    Number of generations, or number of times to evolve the chromosomes;
                             if this is not set, the default value is 100.
        population_size:    Number of chromosomes/individuals in the population for each generation;
                             if this is not set, the default value is 4.
        baseline_accuracy:  Standard to evolve towards, i.e. the accuracy that is ideally achieved
                             after evolving the network num_generations times;
                             if this is not set, the default value is 75%.
                             
        chromosome_len:     Length of an individual, or chromosome, in this case the array storing
                            the operators;
                            if this is not set, the default value is 7.
    """
    
    def __init__(self, num_generations = None, population_size = None, baseline_accuracy = None, chromosome_len = None):
        if num_generations is None:
            self.generations = 10
        else:
            self.generations = num_generations 
        if population_size is None:
            self.pop_size = 10
        else:
            self.pop_size = population_size
        if baseline_accuracy is None:
            self.base_accuracy = 0.75
        else:
            self.base_accuracy = baseline_accuracy
        if chromosome_len is None:
            self.num_genes = 5 #Number of morphological operators, or genes 
        else:
            self.num_genes = chromosome_len
        self.current_accuracy = 0 #Current accuracy of the CNN using the applied morpholigcal operators
        self.current_pop = [0]*self.pop_size #List to keep track of the current most fit chromosomes
        self.mutation_rate = 100 #Likelihood for a mutation on a given gene to occur; large values mean less likely
        self.current_gen = 0
        self.createPop()
        
    def updateCurrentGen(self):
        self.current_gen += 1
        
    def getCurrentGen(self):
        return self.current_gen
    
    def getAccuracy(self):
        return self.current_accuracy

    def setAccuracy(self, accuracy):
        self.current_accuracy = accuracy
        
    def avgAccuracy(self):
        avg = 0
        for i in range(self.pop_size):
            avg = avg + self.currenet_pop[i].getAccuracy()
        avg = avg / self.pop_size
        self.setAccuracy(avg)
    
    def getChromosome(self):
        return self.current_chromosome
        
    def setChromosome(self, chromosome):
        self.current_chromosome = chromosome
    
    def createPop(self):
        for i in range(self.pop_size):
            self.current_pop[i] = ch.chromosome(self.num_genes)
    
    def evaluateFitness(self, accuracy):
       if(accuracy == self.base_accuracy):
           return 1
       else:
           return 0
    
    def updatePop(self):
        self.updateCurrentGen()
        #printAccuracy(self)
        low_accuracies = [[0, 1], [0, 1]] #low_accuracies[0][0] is the index, low_accuracies[0][1] is the accuracy for that index
        high_accuracies = [[0, 0], [0, 0]]
        i = 0
        for b in range(int(self.pop_size/2)):
            if(self.current_pop[i].getAccuracy() < low_accuracies[0][1]):
                low_accuracies[0][0] = i
                low_accuracies[0][1] = self.current_pop[i].getAccuracy()
                #print("New low found")
            if(self.current_pop[i + 1].getAccuracy() < low_accuracies[1][1]):
                low_accuracies[1][0] = i + 1
                low_accuracies[1][1] = self.current_pop[i + 1].getAccuracy()
                #print("Another low found")
            if(self.current_pop[i].getAccuracy() > high_accuracies[0][1]):
                high_accuracies[0][0] = i
                high_accuracies[0][1] = self.current_pop[i].getAccuracy()
                #print("New high found")
            if(self.current_pop[i + 1].getAccuracy() > high_accuracies[1][1]):
                high_accuracies[1][0] = i + 1
                high_accuracies[1][1] = self.current_pop[i + 1].getAccuracy()
                #print("Another high found")            
            i = i + 2
        #print("Low accuracies list is:", low_accuracies)
        #print("High accuracies list is:", high_accuracies)
        parentA = self.current_pop[high_accuracies[0][0]].getChromosome()
        parentB = self.current_pop[high_accuracies[1][0]].getChromosome()
        (childA, childB) = self.crossover(parentA, parentB)
        #print("parentA:", parentA)
        self.current_pop[low_accuracies[0][0]].setChromosome(childA)
        self.current_pop[low_accuracies[1][0]].setChromosome(childB)
        self.current_pop[low_accuracies[0][0]].setAccuracy(0)
        self.current_pop[low_accuracies[1][0]].setAccuracy(0)
        for i in range(self.num_genes): #Randomly mutate a gene in the offspring
            if(random.randint(0, self.mutation_rate) == 10):
                self.current_pop[low_accuracies[0][0]].toggleGene(i)
        for i in range(self.num_genes):
            if(random.randint(0, self.mutation_rate) == 10):
                self.current_pop[low_accuracies[1][0]].toggleGene(i)
        print("Current generation is:", self.getCurrentGen())
        printAccuracy(self)
        self.avgAccuracy()
        print("Average accuracy is:", self.current_accuracy)
    
    def crossover(self, parentA, parentB):
        """
        Crossover point is the 4th element in the list
        Take parentB's first 3 elements and replace parentA's first 3 elements with them
        Take parentA's first 3 elements and replace parentB's first 3 elements with them
        Example: 
            parentA = [1, 2, 3, 4, 5]
            parentB = [100, 200, 300, 400, 500]
            childA = [100, 200, 300, 4, 5]
            childB = [1, 2, 3, 400, 500]
        """
        childA = [0]*self.num_genes
        childB = [0]*self.num_genes
        for i in range(self.num_genes): 
            if i < 3:
                childA[i] = parentB[i]
                childB[i] = parentA[i]
            else:
                childA[i] = parentA[i]
                childB[i] = parentB[i]
        return (childA, childB)

def mutateAndPrint(evolver):
    evolver.mutate()
    printGenes(evolver)

def printGenes(evolver):
    for i in range(evolver.pop_size):
        for j in range(evolver.num_genes):
            print("Chromosome ", i, ", gene ", j, "value is: ", evolver.current_pop[i].getGene(j))
            
def printAccuracy(evolver):
    for i in range(evolver.pop_size):
        print("Chromosome accuracy is:", evolver.current_pop[i].getAccuracy())
