import argparse 
from functools import partial 

import matplotlib.pyplot as plt 
import numpy as np 

from graphics import mutation_fitness_curve, plot
from simulate import create_population, simulate
from variation import sex, mutate

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

    # create the initial population 
    population = create_population(args.n, args.g, params=(args.m * args.g, args.std))
    plot(population) 

    # simulate a timeline with sex/crossover as the variation mechanism 
    sex_history, sex_final_population = simulate(population, args.t, variation=sex)
    plot(sex_final_population)

    # simulate a timeline with mutation as the variation mechanism 
    mutation_history, mutation_final_population = simulate(population, args.t, variation=partial(mutate, p_error=args.e))
    plot(mutation_final_population)

    if args.c is True: 
        # TODO: create cache dir if one does not yet exist (this should really be a parameter to the simulation (not this particular script) 
        np.save("cache/sex_history.npy", history)

    domain = np.linspace(0, args.t, 1000)
    theory_ = list(map(mutation_fitness_curve(args.t, args.g, args.e), domain))

    plt.figure() 
    plt.scatter(sex_history[:, 0], sex_history[:, 1], marker='+', c='g', label='sex/crossover')
    plt.scatter(mutation_history[:, 0], mutation_history[:, 1], marker='+', c='b', label='mutation')
    plt.plot(domain, theory_, linestyle='--', c='k', label="theoretical rate")
    plt.xlabel('Generation') 
    plt.ylabel('Fitness')
    plt.xlim(0, args.t)
    plt.ylim(args.m * args.g - 1, args.g + 1)
    plt.legend() 
    plt.show() 

