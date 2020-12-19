from collections import namedtuple 
from copy import deepcopy
import pdb
from random import shuffle
from typing import Union 

import matplotlib.pyplot as plt 
import numpy as np 
import numpy.random as npr 

Genome = namedtuple('Genome', 'sequence') 

def fitness(genome: Genome, normalized: bool = True) -> int: 
    if normalized is True: 
        return np.sum(genome.sequence)/len(genome.sequence) 
    else: 
        return np.sum(genome.sequence) 

def compute_population_statistics(population: list) -> tuple: 
    fitnesses = np.array([fitness(organism) for organism in population])
    return (fitnesses.mean(), fitnesses.std())

def mutate(genome: Genome, p_error: float) -> Genome: 
    assert 0 <= p_error <= 1, "probability of error must be a float in the interval [0, 1]" 
    mutation = npr.choice([-1, 0], size=len(genome.sequence), p=[p_error, 1 - p_error]) 
    mutated_sequence = abs(genome.sequence + mutation) 
    return Genome(mutated_sequence) 

def crossover(genomes: tuple) -> Genome: 
    father, mother = genomes 
    return Genome(np.array([npr.choice([father.sequence[i], mother.sequence[i]]) for i in range(len(mother.sequence))]))

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
    survivors = selection(children, int(len(children)/2))
    return survivors

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

def selection(population: list, n_survivors: int) -> list: 
    assert n_survivors <= len(population), "number of survivors cannot exceed the population size"
    return sorted(population, key=lambda genome: fitness(genome))[-n_survivors:]

def sex(parents: tuple, n_children: int = 4) -> list: 
    return [crossover(parents) for _ in range(n_children)]

def flip_n(genome: Genome, n_to_flip: int) -> Genome: 
    n = len(genome.sequence)
    assert n_to_flip <= n, "can't flip more bits than exist in the genome" 
    idx_set = npr.choice(list(range(n)), size=n_to_flip, replace=False)
    flipped_sequence = deepcopy(genome.sequence)
    for i in idx_set: 
        flipped_sequence[i] = abs(genome.sequence[i] - 1)
    return Genome(flipped_sequence)

def plot_genome(genome: Union[Genome, list]): 
    if type(genome) == list: 
        n_genomes = len(genome) 
        fig, axs = plt.subplots(ncols=n_genomes) 
        for ax, g in zip(axs, genome): 
            ax.imshow(g.sequence.reshape(-1, 1), cmap="gray")
            ax.set_xticks([]) 
            ax.set_yticks([]) 
        plt.show() 
    else: 
        plt.figure() 
        plt.imshow(genome.sequence.reshape(-1, 1), cmap="gray")
        plt.xticks([]); plt.yticks([])
        plt.show() 

