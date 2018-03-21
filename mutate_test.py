# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:51:18 2018

Tests the mutation function for the morphological_evolver().

@author: etcyl
"""

def mutateAndPrint(evolver):
    evolver.mutate()
    printGenes(evolver)

def printGenes(evolver):
    for i in range(evolver.pop_size):
        for j in range(evolver.num_genes):
            print("Chromosome ", i, ", gene ", j, "value is: ", evolver.current_pop[i].getGene(j))
