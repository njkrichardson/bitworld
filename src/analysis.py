import numpy as np 

from genomics import Genome 

def fitness(genome: Genome, normalized: bool = True) -> int: 
    if normalized is True: 
        return np.sum(genome.sequence)/len(genome.sequence) 
    else: 
        return np.sum(genome.sequence) 

def compute_population_statistics(population: list) -> tuple: 
    fitnesses = np.array([fitness(organism) for organism in population])
    return (fitnesses.mean(), fitnesses.std())
