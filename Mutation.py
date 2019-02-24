import numpy as np
import random as rand

def mutation(populationData, F):    
    oldPopulationData = populationData
    temp = []
    for i in range(np.size(populationData,0)):
        temp.append(i)
    for eachpopulation_colum in range(np.size(populationData,0)):
        r1 = rand.randint(0, np.size(populationData,0)-1) # np.size(populationData,0) = population but this begin 0
        r2 = rand.randint(0, np.size(populationData,0)-1)        
        while r1==eachpopulation_colum or r2==eachpopulation_colum or r1==r2:
            if r1==eachpopulation_colum:
                r1 = rand.randint(0, np.size(populationData,0)-1)
            elif r2==eachpopulation_colum:
                r2 = rand.randint(0, np.size(populationData,0)-1)
            elif r1==r2:
                r1 = rand.randint(0, np.size(populationData,0)-1)        
        for eachpopulation_row in range(np.size(populationData,1)):
            populationData[eachpopulation_colum][eachpopulation_row] = oldPopulationData[eachpopulation_colum][eachpopulation_row] + \
                F * (oldPopulationData[r1][eachpopulation_row] - oldPopulationData[r2][eachpopulation_row])
    return populationData