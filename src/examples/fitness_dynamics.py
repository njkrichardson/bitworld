import argparse 
from functools import partial 
import os 
import pdb 

import matplotlib.pyplot as plt 
import numpy as np 

from constants import RESOLUTION
from graphics import mutation_fitness_curve, plot
from simulate import create_population, simulate
from utils import save
from variation import sex, mutate

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=100, help="number of organisms in the population") 
parser.add_argument("--g", type=int, default=10, help="genome length (in units of bits)") 
parser.add_argument("--t", type=int, default=100, help="timesteps to simulate (a single timestep is the equivalent of simulating a generation") 
parser.add_argument("--m", type=float, default=0.5, help="initial mean of the fitness distribution of the population")
parser.add_argument("--std", type=float, default=0., help="initial standard deviation of the fitness distribution of the population")
parser.add_argument("--e", type=float, default=None, help="mutation error rate (defaults to the 1/(4 * g) where g is the length of the genome")
parser.add_argument("-v", action='store_true', help="whether to print diagnostic information to standard out (verbose mode)") 
parser.add_argument("-c", action='store_true', help="whether to cache the simulation history (saved in the src/cache directory using the time of program execution)")
parser.add_argument("-f", action='store_true', help="whether to produce and save figures from the simulation")
args = parser.parse_args() 

if __name__=="__main__": 

    # create the initial population 
    population = create_population(args.n, args.g, params=(args.m * args.g, args.std))

    # simulate a timeline with sex/crossover as the variation mechanism 
    sex_history, sex_pop_history, sex_final_population = simulate(population, args.t, variation=sex)

    # simulate a timeline with mutation as the variation mechanism 
    mutation_history, mut_pop_history, mutation_final_population = simulate(population, args.t, variation=partial(mutate, p_error=args.e))

    # cache the simulation results (optional) 
    if args.c is True: 
        # TODO what to figure out simulation saving standard (need to keep track of params for analysis) 
        # TODO standardizing simulation history will also streamline graphics creation 
        save(sex_history, verbose=args.v)
        save(mutation_history, verbose=args.v)

    # produce figures (optional) 
    if args.f is True: 

        # initial population versus final population 
        fig, (mutate_ax, sex_ax)= plt.subplots(nrows=2, ncols=2, num=1) 
        plot(population, ax=mutate_ax[0], title='Initial Population', display=False)
        plot(population, ax=sex_ax[0], title='Initial Population', display=False)
        plot(mutation_final_population, ax=mutate_ax[1], title='mutation', display=False)
        plot(sex_final_population, ax=sex_ax[1], title='sex', display=False)

        domain = np.linspace(0, args.t, RESOLUTION)
        theory_ = list(map(mutation_fitness_curve(args.t, args.g, args.e), domain))

        # fitness versus generation index 
        plt.figure(2) 
        plt.scatter(sex_history[:, 0], sex_history[:, 1], marker='+', c='g', label='sex/crossover')
        plt.scatter(mutation_history[:, 0], mutation_history[:, 1], marker='+', c='b', label='mutation')
        plt.plot(domain, theory_, linestyle='--', c='k', label="theoretical rate")
        plt.xlabel('Generation') 
        plt.ylabel('Fitness')
        plt.xlim(0, args.t)
        plt.ylim(args.m * args.g - 1, args.g + 1)
        plt.legend() 
        plt.show() 

