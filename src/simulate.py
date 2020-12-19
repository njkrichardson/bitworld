import pdb 
from random import shuffle

import matplotlib.pyplot as plt 
import numpy as np 
import numpy.random as npr 
from tqdm import tqdm 

from genomics import Genome
from variation import mutate, sex
from analysis import fitness

def select(population: list, n_survivors: int) -> list: 
    assert n_survivors <= len(population), "number of survivors cannot exceed the population size"
    return sorted(population, key=lambda genome: fitness(genome))[-n_survivors:]

def create_population(n_organisms: int, genome_length: int, **kwargs) -> list: 
    assert n_organisms > 0, "number of organisms must be greater than 0" 

    def _create_organism(genome_length: int, **kwargs) -> Genome: 
        assert genome_length > 0, "genome length must be greater than 0" 
        if kwargs.get("params", None) is None: 
            return Genome(npr.choice([0, 1], size=genome_length))
        else: 
            mean, std = kwargs.get("params") 
            return _create_from_params(genome_length, mean, std) 

    return [_create_organism(genome_length, **kwargs) for _ in range(n_organisms)]

def _create_from_params(genome_length: int, mean: float, std: float) -> Genome: 
    organism_fitness = std * npr.randn() + mean 
    if organism_fitness < 0: 
        organism_fitness = 0 
    elif organism_fitness > genome_length: 
        organism_fitness = genome_length
    else: 
        organism_fitness = int(organism_fitness) 
    sequence = np.zeros(genome_length)
    idx_set = npr.choice(list(range(genome_length)), size=organism_fitness, replace=False)
    for i in idx_set: 
        sequence[i] += 1
    return Genome(sequence)

def simulate_generation(population: list, r_0: int = 2, **kwargs): 
    variation = kwargs.get('variation', mutate) 
    if variation == mutate: 
        children = [[variation(parent, **kwargs) for _ in range(r_0)] for parent in population]
    elif variation == sex: 
        shuffle(population) 
        children = [] 
        for i in range(0, len(population)-1, 2): 
            children.append(variation((population[i], population[i+1])))
    children = [child for kids in children for child in kids]
    survivors = select(children, int(len(children)/2))
    return survivors

def fitness_over_time(genome_size: int, sample_size: int, initial_population_size: int, params: tuple, n_generations: int, **kwargs):
    population = create_population(initial_population_size, genome_size, params=params)
    scatter_samples = [] 

    for t in tqdm(range(n_generations)): 
        population = simulate_generation(population, **kwargs)
        if t % 1 == 0: 
            for _ in range(sample_size): 
                idx = npr.choice(np.arange(len(population)))
                g = population[idx]
                scatter_samples.append([t, fitness(g, normalized=False)])

    return np.array(scatter_samples)
