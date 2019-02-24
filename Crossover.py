import numpy as np
import random as rand

def crossover(populationDataOriginal, mutationData, CR):
    crossoverPopulationData = populationDataOriginal.copy()
    for eachpopulationData_colum in range(np.size(populationDataOriginal, 0)):
        for eachpopulationData_row in range(np.size(populationDataOriginal, 1)):
            r = rand.random()            
            if r <= CR:
                crossoverPopulationData[eachpopulationData_colum][eachpopulationData_row] = \
                    mutationData[eachpopulationData_colum][eachpopulationData_row]                
            else:
                pass
    return crossoverPopulationData