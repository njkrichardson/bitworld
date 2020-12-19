from copy import deepcopy 

import numpy.random as npr 

from genomics import Genome 

def corrupt(genome: Genome, n: int) -> Genome: 
    g = len(genome.sequence)
    assert n <= g, "can't flip more bits than exist in the genome" 
    idx_set = npr.choice(list(range(g)), size=n, replace=False)
    flipped_sequence = deepcopy(genome.sequence)
    for i in idx_set: 
        flipped_sequence[i] = abs(genome.sequence[i] - 1)
    return Genome(flipped_sequence)
