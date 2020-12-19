from typing import Union 

import numpy as np
import matplotlib.pyplot as plt

from constants import RESOLUTION
from genomics import Genome 


def plot(genome: Union[Genome, list]): 
    if type(genome) == list: 
        # TODO: maybe just matrixify this
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

def mutation_fitness_curve(n_generations: int, genome_size: int, p_error: float) -> callable: 
    return lambda x: genome_size* (1/2 + 1/(2 * np.sqrt(p_error * genome_size)) * (1 - np.exp(-2 * p_error * x)))

