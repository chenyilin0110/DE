import math
import numpy as np

def fitness(eachPopulationData, dim):
    x = 0
    cos = 0
    for i in range(dim):
        x += pow(eachPopulationData[i], 2)
        cos += math.cos(2 * math.pi * eachPopulationData[i])
    temp = -20 * math.exp(-0.2 * math.sqrt( (1/dim) * x)) - math.exp( (1/dim) * cos)
    calculate = 20 + math.exp(1) + temp    
    return calculate