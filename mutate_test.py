# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:59:03 2018

Test case for the mutateParents() func

@author: etcyl
"""

import genetic

#Two lists of length 7 to act as two chromosomes
X = [1, 2, 3, 4, 5, 6, 7]
Y = [70, 80, 90, 1, 2, 3, 4]

#Create morphological_evolver() class and two children A and B 
m = genetic.morphological_evolver()
(Z, T) = m.mutateParents(X, Y) #Put children A and B into variables Z and T
print("parentA: ", X, "parentB: ", Y)
print("childA: ", Z, "childB: ", T)

#Set 2 out of 4 of the current population to children A and B
m.current_chromosomes[0] = Z
m.current_chromosomes[1] = T
