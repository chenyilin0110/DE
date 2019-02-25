from Fitness import fitness
import numpy as np

def selection(populationDataOriginal, crossoverData, dim):
    selectionPopulationData = populationDataOriginal

    countOriginalFitness = []
    for eachPopulationOriginal in range(np.size(populationDataOriginal,0)):
        countOriginalFitness.append(fitness(populationDataOriginal[eachPopulationOriginal], dim))    
    
    countCrossoverFitness = []
    for eachPopulationCrossover in range(np.size(populationDataOriginal,0)):
        countCrossoverFitness.append(fitness(crossoverData[eachPopulationCrossover], dim))    
    
    for eachPopulation in range(len(countOriginalFitness)):
        if countCrossoverFitness[eachPopulation] <= countOriginalFitness[eachPopulation]:
            for eachDim in range(dim):
                selectionPopulationData[eachPopulation][eachDim] = crossoverData[eachPopulation][eachDim]
        elif countCrossoverFitness[eachPopulation] > countOriginalFitness[eachPopulation]:
            pass    
    return selectionPopulationData