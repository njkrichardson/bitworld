# Why have Sex? 

Bitworld is a collection of Python scripts which allow one to create and analyze the evolutionary dynamics of a customizable "bitworld". 
Bitworld was inspired by David MacKay's _Information Theory, Inference, and Learning Algorithms_ [1]. 

The basic abstraction in bitworld is a Genome, which is a bit-vector representation of an individual organism which is similar to but more abstract than the characteristic lettered genome from standard [genomics](https://en.wikipedia.org/wiki/Genome). Specifically, genomes in bitworld are "gene-valued" rather than "nucleotide-valued" in the sense that the element in the ith index of the vector is a 0 if the organism does not express gene i or 1 if the organism does express gene i. Generations are discrete in bitworld, and the mechanisms for reproductive genetic variation include simple mutation and crossover/sex. Finally, bitworld provides functions to analyze the genetic dynamics of a simulated population; either in terms of the population's genetic diversity or the fitness of the individuals which comprise the population (individually or as a community).

![Population](https://github.com/njkrichardson/bitworld/blob/master/figs/population.png?raw=true)
![Full Sim](https://github.com/njkrichardson/bitworld/blob/master/figs/full_simulation.png?raw=true)
![Fitness v generation](https://github.com/njkrichardson/bitworld/blob/master/figs/fitness_v_generation.png?raw=true)

### References 
[1] MacKay, D. J., & Mac Kay, D. J. (2003). Information theory, inference and learning algorithms. Cambridge university press.
