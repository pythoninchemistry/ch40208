## Sampling Molecular Systems

In the previous exercise, you estimated $\pi$ using uniform sampling: all points in the $2\times2$ square are equally likely.

In molecular systems, however, not all configurations of atoms are equally probable. At thermal equilibrium, the probability of finding a system in state $i$ with energy $E_i$ follows the Boltzmann distribution:

$$P_i = \frac{\exp(-E_i/kT)}{\sum_i \exp(-E_i/kT)} = \frac{\exp(-E_i/kT)}{Z}$$

Here:
- $k$ is Boltzmann's constant
- $T$ is temperature
- $Z$ is the partition function

If we know the energies of all possible states, then we can directly evaluate the partition function, $Z$, and calculate the probability of our system being in each state $i$. We can then use the methods of statistical thermodynamics to directly calculate any thermodynamic averages for our system.

In molecular systems we often have some very large, uncountable number of possible states (configurations) of our system, so we cannot calcuate thermodynamic averages by directly summing over all states.

However, we know that the probability of being in a low energy state is greater than the probability of being in a higher energy state. In principle, if we sample states in a Monte Carlo calculation with probabilities given by their relative Boltzmann factors, then our average over Monte Carlo samples will converge on the true thermodynamic average over all states.

But, to do this, it seems we need to calculate the probability of being in state $i$, which (from above) requires that we know the partition function $Z$. And we need to sum over all states to evaluate the partition function. So we seem to be stuck.
