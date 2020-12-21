import pdb
from typing import Tuple

import numpy as np
import numpy.random as npr

from genomics import Genome 

def mutate(genome: Genome, p_error: float = None) -> Genome: 
    if p_error is None: 
        g = len(genome.sequence)
        p_error = 1 / (4 * g) 
    assert 0 <= p_error <= 1, "probability of error must be a float in the interval [0, 1]" 
    mutation = npr.choice([-1, 0], size=len(genome.sequence), p=[p_error, 1 - p_error]) 
    mutated_sequence = abs(genome.sequence + mutation) 
    return Genome(mutated_sequence) 

def crossover(parents: Tuple[float, float]) -> Genome: 
    father, mother = parents
    return Genome(np.array([npr.choice([father.sequence[i], mother.sequence[i]]) for i in range(len(mother.sequence))]))

def sex(parents: Tuple[Genome, Genome], n_children: int = 4) -> list: 
    return [crossover(parents) for _ in range(n_children)]
