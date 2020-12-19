from copy import deepcopy 
from datetime import datetime
from os import mkdir
from os.path import join, exists
from pathlib import Path 

import numpy as np 
import numpy.random as npr 

from constants import CACHE_PATH
from genomics import Genome 

def get_project_root() -> Path:
    """https://bit.ly/2IeOzo8""" 
    return Path(__file__).parent.parent

def save(arr: np.ndarray, filename: str = None, verbose: bool = False): 
    try: 
        # TODO: param config? 
        now = datetime.utcnow().strftime('%H:%M:%S_%d_%b_%Y')
        if exists(CACHE_PATH) is not True: 
            mkdir(CACHE_PATH) 
        if filename is None: 
            filename = now
        else:
            '_'.join([now, filename]) 
        save_path = join(CACHE_PATH, filename)
        np.save(save_path, arr)
        if verbose is True: print(f"Saved array to {save_path}.npy")
    except Exception as e: 
        if verbose is True: 
            print(e)

def corrupt(genome: Genome, n: int) -> Genome: 
    g = len(genome.sequence)
    assert n <= g, "can't flip more bits than exist in the genome" 
    idx_set = npr.choice(list(range(g)), size=n, replace=False)
    flipped_sequence = deepcopy(genome.sequence)
    for i in idx_set: 
        flipped_sequence[i] = abs(genome.sequence[i] - 1)
    return Genome(flipped_sequence)
