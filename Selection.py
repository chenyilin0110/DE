from Fitness import fitness
import numpy as np

def selection(populationDataOriginal, crossoverData, dim):
    selectionPopulationData = populationDataOriginal

    countOriginalFitness = []
    countCrossoverFitness = []
    for eachPopulation in range(np.size(populationDataOriginal,0)):
        countOriginalFitness.append(fitness(populationDataOriginal[eachPopulation], dim))
        countCrossoverFitness.append(fitness(crossoverData[eachPopulation], dim))    
    
    for eachPopulation in range(len(countOriginalFitness)):
        if countCrossoverFitness[eachPopulation] <= countOriginalFitness[eachPopulation]:
            for eachDim in range(dim):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
        elif countCrossoverFitness[eachPopulation] > countOriginalFitness[eachPopulation]:
            pass
    return selectionPopulationData