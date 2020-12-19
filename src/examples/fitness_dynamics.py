import argparse 
from functools import partial 

import matplotlib.pyplot as plt 
import numpy as np 

from graphics import mutation_fitness_curve, plot
from simulate import create_population, simulate
from variation import sex 

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=100, help="number of organisms in the population") 
parser.add_argument("--g", type=int, default=10, help="genome length (in units of bits)") 
parser.add_argument("--t", type=int, default=100, help="timesteps to simulate (a single timestep is the equivalent of simulating a generation") 
parser.add_argument("--m", type=float, default=0.5, help="initial mean of the fitness distribution of the population")
parser.add_argument("--std", type=float, default=0., help="initial standard deviation of the fitness distribution of the population")
parser.add_argument("--e", type=float, default=None, help="mutation error rate (defaults to the 1/(4 * g) where g is the length of the genome")
parser.add_argument("--v", action='store_true', help="whether to print diagnostic information to standard out (verbose mode)") 
parser.add_argument("--c", action='store_true', help="whether to cache the simulation history (saved in the src/cache directory using the time of program execution)")
args = parser.parse_args() 

if __name__=="__main__": 
    # fitness over time 
    sample_size = 6
    params = (args.m * args.g, args.std)
    
    if args.e is None: 
        p_error = 1/(4 * args.g)

    # create the initial population 
    population = create_population(args.n, args.g, params=params)
    plot(population) 
    history, final_population = simulate(population, args.t, p_error=args.e, variation=sex)
    plot(final_population)

    if args.c is True: 
        # TODO: create cache dir if one does not yet exist (this should really be a parameter to the simulation (not this particular script) 
        np.save("cache/sex_history.npy", history)

    domain = np.linspace(0, args.g, 1000)
    theory_ = list(map(partial(mutation_fitness_curve, args.g, args.e), domain))

    plt.figure() 
    plt.scatter(history[:, 0], history[:, 1], marker='+', c='k')
    # plt.plot(domain, list(map(theory, domain)), linestyle='--', c='k')
    plt.xlabel('Generation') 
    plt.ylabel('Fitness')
    plt.xlim(0, args.t)
    plt.ylim(500, 1000)
    plt.show() 



