import pdb 

import matplotlib.pyplot as plt 
import numpy as np 
import numpy.random as npr 
from tqdm import tqdm 

from sex import Genome, create_population, simulate_generation, fitness, sex

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

if __name__=="__main__": 

    # fitness over time 
    genome_size = 1000
    sample_size = 6
    n_generations = 100
    initial_population_size = 1000 
    init_mean, init_std = 0.5 * genome_size, 0
    params = (init_mean, init_std)
    p_error = 1/(4 * genome_size)
    variation = sex

    history = fitness_over_time(genome_size, sample_size, initial_population_size, params, n_generations, p_error=p_error, variation=variation)
    np.save("sex_history.npy", history)

    domain = np.linspace(0, n_generations, 1000)
    theory = lambda x: genome_size* (1/2 + 1/(2 * np.sqrt(p_error * genome_size)) * (1 - np.exp(-2 * p_error * x)))
    theory_ = list(map(theory, domain))

    plt.figure() 
    plt.scatter(history[:, 0], history[:, 1], marker='+', c='k')
    # plt.plot(domain, list(map(theory, domain)), linestyle='--', c='k')
    plt.xlabel('Generation') 
    plt.ylabel('Fitness')
    plt.ylim(500, 1000)
    plt.show() 

