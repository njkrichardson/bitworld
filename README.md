# Why have Sex? 

Bitworld is a collection of Python modules which enable the simulation and analysis of the evolutionary dynamics of a customizable "bitworld". Models of evolutionary genetics are used to understand information acquisition and evolution (here "information" refers to the [unambiguous concept](https://en.wikipedia.org/wiki/Information_theory) from mathematical information theory rather than the colloquial usage). Ultimately the scientific desideratum is an understanding of the evolution of genetic systems obtained by "reverse engineering" Nature's software stack. 

## Contents
 
### Background 
* [Information acquisition and evolution](#information-acquisition-and-evolution)
* [Evolution of genetic systems for computer scientists](#evolution-of-genetic-systems-for-computer-scientists) 

### Bitworld
* [Installation and Quickstart](#installation-and-quickstart)
* [A simple example](#a-simple-example)

[References](#references)

### Information acquisition and evolution

Genomes are apparently _acquiring_ information over time; consider that the entire program to construct an organism is the result of a deceptively simple teaching process in which natural selection is the teacher. 

> Thanks to the tireless work of the Blind Watchmaker, some cells now carry within them all
the information required to be outstanding spiders; other cells carry all the
information required to make excellent octopuses. Where did this information
come from? [1]

The teaching signal or 'supervision signal' in evolution acts to evaluate the fitness (informally, the propensity for an individual to reproduce viable offspring) of an organism as a function of the organism's DNA and environment. Surprisingly, this teaching signal is very weak: just a few bits of information per individual [1]. The teaching signal also does not communicate to the organism or the broader ecosystem any information about _why_ an organism's children or grandchildren survived (or didn't). Finally, since the teaching signal is highly redundant (many individuals will fail to have offspring for similar reasons), it's curious that such an impoverished learning algorithm gave rise to the biological complexity we observe empirically. Simulation and analysis tools like bitworld wield computational and mathematical methods to explore this information transfer, and a variety of other interesting questions: 

 * Why have Sex? Put another way, what are the implications of genetic systems in which organisms reproduce parthogenetically (asexually) versus sexually? 
 * Why have two sexes? Why not three or seven? 
 * How can we characterize the distribution of fitness across a population in which the mechanism to introduce genetic variation is mutation versus sex/crossover? 
 * How many bits per generation are acquired by the species as a whole
by natural selection?
 * What is the relationship between the genetic variation mechanism and resilience to genetic mutations? 

### Evolution of genetic systems for computer scientists
 
One way to understand the evolution of genetic systems is as a simple learning algorithm in which mechanisms like mutation and crossover introduce variations in genetic systems over time; these variations introduce generational perturbations in the genome which in turn affect the fitness of organism. 

---
<p align="center">
<img src="https://github.com/njkrichardson/bitworld/blob/master/figs/perspective.png" alt="drawing" width="500"/>
</p>

---

Consider that assuming an uncompressed file size of approximately 1 GB per human genome, one could store the instructions to construct the entire population of [Joseph, OR](https://en.wikipedia.org/wiki/Joseph,_Oregon) on the thumb drive shown below<sup>1</sup>. 

<p align="center">
  <img src="https://github.com/njkrichardson/bitworld/blob/master/figs/terabyte_microsd.png" alt="drawing" width="200"/>
</p>

The representation of an organism's genome is straightforward, below I illustrate an example with "nucleotide-valued" bit-vectors. That is, a finite ordered list of 0s and 1s which encode the characteristic "lettered" nucleotide representations (e.g., in the human genome, the letter codes for the four constituent nucleotides). The human genome contains four distinct nucleotides, so we need two bits to represent each unique code and thus the bit-vector representation of a lettered genome is twice the length (two bits per letter in the original genome). Additionally, I formalize the domains and codomains of the functional aspects of evolution (the simple model shows specific instantiations of these functions). 

<p align="center">
  <img src="https://github.com/njkrichardson/bitworld/blob/master/figs/types.png" alt="drawing" width="700"/>
</p>

### Installation and Quickstart 

Install bitworld with the following command from your command line interface: 

```bash 
$ git clone https://github.com/njkrichardson/bitworld.git
```

The basic abstraction in bitworld is a Genome, which is a bit-vector representation of an individual organism which is similar to but more abstract than the characteristic lettered genome from standard [genomics](https://en.wikipedia.org/wiki/Genome). Specifically, genomes in bitworld are "gene-valued" rather than "nucleotide-valued" in the sense that the element in the ith index of the vector is a 0 if the organism does not express gene i or 1 if the organism does express gene i. Generations are discrete in bitworld, and the mechanisms for reproductive genetic variation include simple mutation and crossover/sex. Finally, bitworld provides functions to analyze the genetic dynamics of a simulated population; either in terms of the population's genetic diversity or the fitness of the individuals which comprise the population (individually or as a community).

Genome's are namedtuples with a single field named "sequence" which is a [NumPy](https://en.wikipedia.org/wiki/NumPy) array comprised of only 0s and 1s. Numpy was chosen so that the package can be expanded to include more powerful simulations, fitness functions, numerical representations of genomes, etc. 

### A simple example 

The figures below were generated by running `examples/fitness_variation.py`. In the first image we show a visual representation of the population genome (that is, the genome of every individual in the population). Each rectangular binary image represents a snapshot of the population genome at a point in the simulated timeline; for example the images in the third column display the genome of the populations after 7 generations (and just before the 8th). Each row of the binary image indexes a particular gene; the ith row corresponds to gene i. The columns of the binary image index individuals in the population; the jth column corresponds to individual j. That is, the element in row 2 column 8 corresponds to the genetic status of the 8th individual in the population with respect to the 2nd gene in our genome. This element will be a 1 (or fill the image sector white) when the organism has a good copy of the gene, and a 0 (or fill the image sector black) when the organism has a defective copy of the gene.

<p align="center">
  <img src="https://github.com/njkrichardson/bitworld/blob/master/figs/population.png" alt="drawing" width="800"/>
</p>

Even after 50 generations, the population which introduces genetic variation in subsequent generations through mutation only has still not obtained eugenic perfection (maximal fitness). 

<p align="center">
  <img src="https://github.com/njkrichardson/bitworld/blob/master/figs/full_simulation.png" alt="drawing" width="500"/>
</p>

Finally, we can plot the history of the simulation, specifically the average fitness of the population versus the number of simulated generations. The genome acquires information at a significantly higher rate when variation is introduced via sex/crossover.

<p align="center">
  <img src="https://github.com/njkrichardson/bitworld/blob/master/figs/fitness_v_generation.png" alt="drawing" width="600"/>
</p>

### References 
Bitworld was inspired by David MacKay's chapter "Why have Sex?" in _Information Theory, Inference, and Learning Algorithms_

[1] MacKay, D. J., & Mac Kay, D. J. (2003). Information theory, inference and learning algorithms. Cambridge university press.

---
[1] A technical note here is that the data coming off of sequencers is in practice much greater than 1GB to enable error correction and reconstruction (in practice the file sizes are on the order of hundreds of GB) but in principle this factoid is still reasonable. If we allow for compression, things get even stranger. 
