## Monte Carlo Simulation of the 1D Ising Model

In this exercise, you'll implement a Monte Carlo simulation of a 1D Ising model with 4 spins and periodic boundary conditions. We'll build this up in steps, eventually calculating the mean magnetisation as a function of temperature.


The one-dimensional Ising model consists of a line of spins that can each take values $\sigma_i = \pm1$ (up or down). The total energy of the system depends on the relative orientations of neighbouring spins, according to:

$$H(\sigma) = -\sum_{<ij>} J_{ij}\sigma_i\sigma_j$$

where the sum runs over adjacent pairs $i$ and $j$ and $J_{ij}$ is the coupling constant between spins $i$ and $j$.

Consider a simple model system with only four spins. We make our system periodic so that spins 1 and 4 are neighbours (every spin neighbours two other spins).

This system has a total of $2^4=16$ spin states. There are two degenerate states with all spins parallel, with enegy $-4J$, two degenerate states with alternating up and down spins, with energy $+4J$, and 12 degenerate states with both parallel and anti-parallel adjacent spins: these all have energy $0J$. For each of these spin states we can also calculate the total magnetisation, $|m|$, as the difference between the numbers of up and down spins.

```{figure} ./figures/4_spin_ising_model.png
---
width: 350px
---
The four inequivalent states of a 4-spin Ising model, showing their spin configurations, energies, and magnetisation.
```

Consider the problem of calculating the average absolute magnetisation $\left<M\right>$ as a function of temperature? Four our 4-spin system we can compute this directly using statistical mechanics:

$$\left<M\right> = \sum_i \frac{\left|m_i\right|g_i\exp\left(-E_i/kT\right)}{Z}$$

where $Z$ is the usual partition function $Z = \sum_i \exp\left(-E_i/kT\right)$, and $g_i$ is the degeneracy of the $i$<sup>th</sup> state.

For example, evaluating this gives $\left<M\right> = 1.5$ in the high-T limit ($T\to\infty$).

You can also numerically simulate this system using Metropolois Monte Carlo.

### Part 1. Energy Calculation
Write a function that calculates the energy of a periodic 1D Ising model. You should represent the spin-state of your system using a numpy array where every element is either $+1$ (spin-up) or $-1$ (spin-down). Your function will take as input a single spin state and $J$. Test your function by passing the following numpy arrays, which correspond to the four inequivalent spin configurations of a 4-spin system (Use $J = 0.012$ eV).:
```python
np.array([-1,1,-1,1]) # E = +4J
np.array([-1,-1,1,1]) # E = 0J
np.array([1,1,-1,1])  # E = 0J
np.array([1,1,1,1])   # E = -4J
```

### Part 2: Single Monte Carlo Step

Implement a single MC step that:
1. Picks a random spin.
2. Calculates $\Delta E$ for flipping this spin.
3. Accepts/rejects the flip using the Metropolis criterion.

### Part 3: Magnetisation

The magnetisation is simply the sum of the spins. Implement a function to calculate the absolute magnetisation per spin. Your function should take a single numpy array describing the spin-state as the argument.

### Part 4: Full Simulation

Now combine these pieces to simulate the system at 1000 K.

1. Perform $N$ MC steps, where each step you propose a random spin flip and accept or reject using the Metropolis criterion
2. For each step, whether you accept or reject the move, calculate the magnetisation.
3. Your mean magnetisation is then the mean value over all MC steps. As for the previous exercise, your calculation will progressively converge its estimate of $\left<M\right>$ as you increase the number of MC steps. Evaluate what a reasonable value of $N$ is to converge your estimate of the mean magnetisation to 2 decimal places.


### Part 5: Temperature Dependence

Wrap your entire simulation in a function that takes as arguments the temperature $T$ and $J$.
By calling this function from a loop, run simulations at a range of temperatures from 0 K to 2000 K.
Plot the mean magnetisation versus temperature, and compare to the high-temperature limit value.

(Bonus: write a function to calculate the exact magnetisation using the statistical mechanical expression given above. Plot this exact result on the same plot as your simulation data to compare the two.)

```{figure} ./figures/ising_MC_results.png
---
width: 350px
---
Plot of mean magnetisation for a 4-spin Ising model ($J$ = 0.012 eV) as a function of temperature, calculated using Metropolis Monte Carlo and compared to the exact result.
```
