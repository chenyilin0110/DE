import numpy as np
import random as rand
import sys
from Mutation import mutation
from Crossover import crossover
from Selection import selection
from Fitness import fitness
Ud = sys.argv[1]
population = sys.argv[2]
dim = sys.argv[3]
F = sys.argv[4]
CR = sys.argv[5]
iteration = sys.argv[6]

Ld = float(Ud) * (-1)

# Initial 
populationDataOriginal = np.zeros((int(population), int(dim)))
for eachpopulationData_colum in range(int(population)):
    for eachpopulationData_row in range(int(dim)):
        r = rand.random()
        populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = ((float(Ud) - Ld) * r) + Ld
populationData = populationDataOriginal.copy() # copy populationDataOriginal to populationData
best = 99999
for eachiteration in range(int(iteration)):
	# Mutation
	mutationData = mutation(populationData, float(F))

	# Crossover
	crossoverData = crossover(populationDataOriginal, mutationData, float(CR))

	# Selection
	selectionData = selection(populationDataOriginal, crossoverData, int(dim))			
	count = []
	for i in range(np.size(selectionData, 0)):
		count.append(fitness(selectionData[i][:], int(dim)))
		if count[i] < best:
			best = count[i]
	print(eachiteration, best)
	# reset
	populationDataOriginal = selectionData.copy()
	populationData = selectionData.copy()