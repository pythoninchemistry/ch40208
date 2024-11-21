# Monte Carlo Simulation in Computational Chemistry

## Introduction

In molecular dynamics, we model chemical systems by numerically integrating equations of motion to generate trajectories through time. Starting with atomic positions and velocities at time $t$, we calculate the forces, update positions and velocities, and repeat this process to simulate molecular motion. However, there are several situations where this approach becomes problematic:

1. We might not be able to calculate the forces $F(r)$ required for MD. This could be because force evaluation is computationally expensive, or because the forces are not well-defined for our system.

2. The timescale of important transitions might be much longer than we can practically simulate. For example, protein folding or chemical reactions with high activation barriers can take milliseconds or longer, while MD timesteps are typically femtoseconds.

3. Our system might have a discrete, rather than continuous, configuration space. Consider a lattice model where molecules occupy specific sites, or magnetic systems where spins point only up or down.

Monte Carlo simulation offers an alternative approach. Rather than following the detailed dynamics of molecular motion, Monte Carlo methods use random sampling to explore configuration space and calculate equilibrium properties. This can overcome many of the limitations of molecular dynamics, at the cost of losing information about true dynamical behavior.

## Exercise 1: Monte Carlo Integration - Calculating π

To understand the principles of Monte Carlo methods, let's consider a simple but illuminating problem: calculating the area of a circle and thus the value of π. Analytically, we can find a circle's area by imagining it divided into infinitesimally thin concentric rings. The area of each ring is its circumference (2πr) multiplied by its thickness (dr):

$A_{circle} = \int_0^R 2\pi r\,dr = \pi R^2$

But what if we couldn't perform this integration analytically? This is often the case in molecular systems, where we need to integrate over complex, high-dimensional configuration spaces. Monte Carlo methods provide a powerful alternative approach.

Consider a unit circle ($R=1$) inscribed in a 2×2 square. The ratio of their areas is:

$\frac{A_{circle}}{A_{square}} = \frac{\pi R^2}{(2R)^2} = \frac{\pi}{4}$

We can estimate this ratio - and thus π - using random sampling. This demonstrates a key principle of Monte Carlo integration: we can approximate integrals by randomly sampling the integration space and counting the fraction of samples that meet certain criteria.

### Implementation Task

Your task is to implement the Monte Carlo estimation of π using random sampling. The mathematical approach is:
1. The ratio of points inside the circle to total points estimates $A_{circle}/A_{square}$
2. We know $A_{circle}/A_{square} = \pi/4$
3. Therefore π = 4 × (points inside circle)/(total points)

You'll need these Python tools:
```python
# For random number generation and array operations
import numpy as np
from numpy.random import uniform

# Generate N points at once - returns array of shape (N,2)
points = uniform(low=-1, high=1, size=(N,2))
# points[:,0] gives x coordinates
# points[:,1] gives y coordinates

# Calculate r^2 for all points at once
r_squared = points[:,0]**2 + points[:,1]**2

# For plotting
import matplotlib.pyplot as plt
```

Complete this Python function that implements the method:

```python
def estimate_pi(N):
    """
    Estimate π using Monte Carlo sampling.
    
    Parameters
    ----------
    N : int
        Number of random points to generate
        
    Returns
    -------
    float
        Estimate of π
    """
    # Generate N random points in square
    points = uniform(low=-1, high=1, size=(N,2))
    
    # Your code here:
    # 1. Calculate r² for all points: points[:,0]**2 + points[:,1]**2
    # 2. Count how many points have r² ≤ 1 (inside circle)
    # 3. Calculate π as 4 × (points inside)/(total points)
    
    return pi_estimate
```

For visualization, use this provided function:
```python
def plot_monte_carlo(N):
    """Generate a plot showing Monte Carlo estimation of π.
    
    Creates a square plot with a unit circle and plots N random points,
    colored according to whether they fall inside or outside the circle.
    
    Args:
        N (int): Number of random points to generate
        
    Returns:
        float: Estimate of π from this sampling
    """
    # Set up the plot with circle
    plt.axes()
    circle = plt.Circle((0,0), radius=1.0, fc='white', ec="green")
    plt.gca().add_patch(circle)
    plt.axis('scaled')
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    
    # Generate N random points
    points = uniform(low=-1.0, high=1.0, size=(N,2))
    
    # Count points inside circle and plot all points
    n_inside = 0
    for x, y in points:
        if x**2 + y**2 < 1.0:
            plt.plot(x, y, 'o', color='red', alpha=0.5, markersize=5)
            n_inside += 1
        else:
            plt.plot(x, y, 'o', color='blue', alpha=0.5, markersize=5)
    
    # Calculate and display π estimate
    pi_estimate = 4.0 * n_inside / N
    plt.title(r"$\pi \approx $" + f"{pi_estimate:.4f}", loc="right")
    plt.title(f"{N} samples", loc="left")
    
    plt.show()
    return pi_estimate
```

After implementing the function:
1. Test your estimation with different numbers of points:
   ```python
   for N in [50, 500, 5000, 50000]:
       pi_est = estimate_pi(N)
       print(f"N = {N:6d}: π ≈ {pi_est:.6f}, error = {abs(pi_est - np.pi):.6f}")
   ```

2. Visualize the sampling for each N using `plot_monte_carlo(N)`

3. Record your results in this table:

| N | π estimate | Absolute Error |
|---|------------|---------------|
| 50 | | |
| 500 | | |
| 5000 | | |
| 50000 | | |

#### Analysis Questions
1. How does the accuracy improve with N?
2. Why do you get different results each time you run the code?
3. What N would you need for 2 decimal place accuracy?
4. How does this generalize to other integration problems?

This example illustrates key features of Monte Carlo methods:
- Statistical errors decrease with increased sampling
- Results are inherently probabilistic
- The method can handle integrals that are difficult analytically
- The approach generalizes to higher dimensions

## Statistical Mechanics and the Boltzmann Distribution

In molecular systems, not all configurations are equally probable. At thermal equilibrium, the probability of finding a system in state i with energy $E_i$ follows the Boltzmann distribution:

$$P_i = \frac{\exp(-E_i/kT)}{\sum_i \exp(-E_i/kT)} = \frac{\exp(-E_i/kT)}{Z}$$

Here:
- $k$ is Boltzmann's constant
- $T$ is temperature
- $Z$ is the partition function

This presents two practical challenges:
1. We need to preferentially sample low-energy states
2. We cannot calculate Z directly as it requires summing over all possible states

## The Metropolis Algorithm

The Metropolis algorithm provides an elegant solution to these sampling problems. Rather than trying to calculate absolute probabilities, it works with probability ratios:

Starting from a configuration i:
1. Propose a random move to configuration j
2. Calculate the energy change ΔEij = Ej - Ei
3. Accept the move with probability:

$$A(i \rightarrow j) = \min(1, \exp(-\Delta E_{ij}/kT))$$

This acceptance criterion ensures:
- Moves that lower energy (ΔE < 0) are always accepted
- Moves that raise energy are accepted with probability exp(-ΔE/kT)
- The partition function Z cancels out in the ratio

## Exercise 2: Monte Carlo Simulation of the 1D Ising Model

In this exercise, you'll implement a Monte Carlo simulation of a 1D Ising model with 4 spins and periodic boundary conditions. We'll build this up in steps, eventually calculating the mean magnetization as a function of temperature.

### Part 1: System Energy

The one-dimensional Ising model consists of a line of spins that can each take values σi = ±1 (up or down). The Hamiltonian is:

$$H(\sigma) = -\sum_{<ij>} J_{ij}\sigma_i\sigma_j$$

where the sum runs over adjacent pairs and Jij is the coupling constant between spins i and j.

For ferromagnetic coupling (J > 0):
- Adjacent spins prefer to align parallel at low temperature
- Thermal fluctuations increasingly randomize the spins at higher temperature

#### Understanding Periodic Boundary Conditions

With periodic boundary conditions, we connect the ends of the chain to form a ring:
- The last spin (N) is considered adjacent to the first spin (1)
- This means spin N interacts with both spin N-1 and spin 1
- We can think of this as "wrapping" our 1D system around a circle

For our 4-spin system:
```
Regular chain:    σ₁ -- σ₂ -- σ₃ -- σ₄
With periodic:    σ₁ -- σ₂ -- σ₃ -- σ₄
                 |___________________|
```

The Ising Hamiltonian with these boundary conditions is:

$H(\sigma) = -J\sum_{i=1}^N \sigma_i\sigma_{i+1}$

where $\sigma_{N+1} \equiv \sigma_1$ (periodic boundary), and each spin $\sigma_i = \pm 1$.

```python
def calculate_energy(spins, J):
    """Calculate the energy of a 1D Ising model configuration.
    
    Args:
        spins (array): Array of spins (±1)
        J (float): Coupling constant
        
    Returns:
        float: Energy of the configuration
    """
    # Your code here:
    # 1. Sum over neighboring spin pairs
    # 2. Remember periodic boundary conditions
    # 3. Return -J × sum(σᵢσᵢ₊₁)
```

Test your function with these configurations:
```python
spins_up = np.ones(4)      # All spins up
spins_alt = np.array([1, -1, 1, -1])  # Alternating spins
```

### Part 2: Single Monte Carlo Step

Implement a single MC step that:
1. Picks a random spin
2. Calculates ΔE for flipping this spin
3. Accepts/rejects the flip using the Metropolis criterion

```python
def monte_carlo_step(spins, J, kT):
    """Perform one Monte Carlo step using Metropolis algorithm.
    
    Args:
        spins (array): Current spin configuration
        J (float): Coupling constant
        kT (float): Temperature (in units of J)
        
    Returns:
        array: Updated spin configuration
    """
    # Your code here:
    # 1. Choose random spin
    # 2. Calculate energy change for flip
    # 3. Accept with probability min(1, exp(-ΔE/kT))
```

### Part 3: Magnetization

The magnetization is simply the sum of the spins. Implement a function to calculate the absolute magnetization per spin:

```python
def magnetization(spins):
    """Calculate absolute magnetization per spin.
    
    Args:
        spins (array): Spin configuration
        
    Returns:
        float: |M|/N where M = sum(spins)
    """
    return np.abs(np.sum(spins))/len(spins)
```

### Part 4: Full Simulation

Now combine these pieces to simulate the system at different temperatures:

```python
def run_ising_simulation(N_spins=4, J=0.012, kT=0.025, N_steps=1000):
    """Run Ising model simulation.
    
    Args:
        N_spins (int): Number of spins
        J (float): Coupling constant (eV)
        kT (float): Temperature (eV)
        N_steps (int): Number of Monte Carlo steps
        
    Returns:
        float: Mean absolute magnetization for this temperature
    """
    # Initialize all spins up
    spins = np.ones(N_spins)
    
    # Equilibration
    for _ in range(N_steps//2):
        spins = monte_carlo_step(spins, J, kT)
    
    # Production and measurement
    mag = 0.0
    for _ in range(N_steps//2):
        spins = monte_carlo_step(spins, J, kT)
        mag += magnetization(spins)
    
    return mag/(N_steps//2)
```

### Part 5: Temperature Dependence

Finally, let's calculate magnetization vs. temperature:

```python
# Temperature range (in Kelvin)
T = np.linspace(10, 2000, 50)
kT = T * 8.617e-5  # Convert to eV

# Calculate magnetization for each temperature
mag_vs_T = [run_ising_simulation(kT=kt) for kt in kT]

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(T, mag_vs_T, 'o-')
plt.xlabel('Temperature (K)')
plt.ylabel('Mean magnetization per spin')
plt.grid(True)
```

### Analysis Questions
1. What happens to the magnetization at very low temperatures? Why?
2. At what temperature does the system start to lose its magnetization?
3. What is the high-temperature limit of the magnetization? Why?
4. How would increasing the number of Monte Carlo steps affect your results?

### Extra Challenges
1. Add error bars to your magnetization measurements
2. Calculate other properties (e.g., energy, specific heat)
3. Investigate how the results change with system size
4. Compare your results to the exact solution for the 1D Ising model
