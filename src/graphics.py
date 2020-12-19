from typing import Union 

import numpy as np
import matplotlib.pyplot as plt

from constants import RESOLUTION
from genomics import Genome 

def plot(genome: Union[Genome, list]): 
    plt.figure()
    if type(genome) == list: 
        m, n = len(genome), len(genome[0].sequence)
        genome_arr = np.empty((n, m), dtype=int, order='C')
        for i, g in enumerate(genome): 
            genome_arr[:, i] = g.sequence

        plt.imshow(genome_arr, cmap="gray") 
    else: 
        plt.imshow(genome.sequence.reshape(-1, 1), cmap="gray")

    plt.xticks([]) 
    plt.yticks([]) 
    plt.show() 

def mutation_fitness_curve(n_generations: int, genome_size: int, p_error: float) -> callable: 
    return lambda x: genome_size* (1/2 + 1/(2 * np.sqrt(p_error * genome_size)) * (1 - np.exp(-2 * p_error * x)))

