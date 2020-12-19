# Why have Sex? 

Bitworld is a collection of Python modules which enable the simulation and analysis of the evolutionary dynamics of a customizable "bitworld". Models of evolutionary genetics are used to understand information acquisition and evolution (here "information" refers to the [unambiguous concept](https://en.wikipedia.org/wiki/Information_theory) from mathematical information theory rather than the colloquial usage). Ultimately the scientific desideratum is an understanding of the evolution of genetic systems obtained by "reverse engineering" Nature's software stack. 

## Contents
 
### Background 
* Information acquisition and evolution
* Evolution of genetic systems for computer scientists 
* Rate of increase of fitness
* A simple model 

### Bitworld
* Installation and Quickstart 
* A simple example 

References

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

The basic abstraction in bitworld is a Genome, which is a bit-vector representation of an individual organism which is similar to but more abstract than the characteristic lettered genome from standard [genomics](https://en.wikipedia.org/wiki/Genome). Specifically, genomes in bitworld are "gene-valued" rather than "nucleotide-valued" in the sense that the element in the ith index of the vector is a 0 if the organism does not express gene i or 1 if the organism does express gene i. Generations are discrete in bitworld, and the mechanisms for reproductive genetic variation include simple mutation and crossover/sex. Finally, bitworld provides functions to analyze the genetic dynamics of a simulated population; either in terms of the population's genetic diversity or the fitness of the individuals which comprise the population (individually or as a community).

![Population](https://github.com/njkrichardson/bitworld/blob/master/figs/population.png?raw=true)
![Full Sim](https://github.com/njkrichardson/bitworld/blob/master/figs/full_simulation.png?raw=true)
![Fitness v generation](https://github.com/njkrichardson/bitworld/blob/master/figs/fitness_v_generation.png?raw=true)

### References 
Bitworld was inspired by David MacKay's chapter "Why have Sex?" in _Information Theory, Inference, and Learning Algorithms_

[1] MacKay, D. J., & Mac Kay, D. J. (2003). Information theory, inference and learning algorithms. Cambridge university press.

---
[1] A technical note here is that the data coming off of sequencers is in practice much greater than 1GB to enable error correction and reconstruction (in practice the file sizes are on the order of hundreds of GB) but in principle this factoid is still reasonable. If we allow for compression, things get even stranger. 
