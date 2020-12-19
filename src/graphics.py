from typing import Sequence
from typing import Union 
import pdb

import numpy as np
import matplotlib.pyplot as plt

from constants import RESOLUTION
from genomics import Genome

def plot(genome: Union[Genome, Sequence[Genome]], display: bool = True, ax = None, **kwargs): 
    title = kwargs.get("title", None)
    if ax is None: 
        plt.figure() 
        ax = plt
        plt.xticks([])
        plt.yticks([])
    else: 
        ax.set_xticks([]) 
        ax.set_yticks([]) 

    if type(genome) == list: # TODO generalize 
        m, n = len(genome), len(genome[0].sequence)
        genome_arr = np.empty((n, m), dtype=int, order='C')
        for i, g in enumerate(genome): 
            genome_arr[:, i] = g.sequence

        ax.imshow(genome_arr, cmap="gray", vmin=0, vmax=1) 
    else: 
        ax.imshow(genome.sequence.reshape(-1, 1), cmap="gray", vmin=0, vmax=1,  **kwargs)

    if kwargs.get("title", None) is not None: 
        # TODO may be an edge case here when ax is instantiated via plt.figure() 
        ax.set_title(kwargs.get("title")) 

    if display is True: 
        ax.show() 

    return ax 

def mutation_fitness_curve(n_generations: int, genome_size: int, p_error: float) -> callable: 
    if p_error is None: 
        p_error = 1/(4 * genome_size)
    return lambda x: genome_size* (1/2 + 1/(2 * np.sqrt(p_error * genome_size)) * (1 - np.exp(-2 * p_error * x)))

