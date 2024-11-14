## Exercises

### Aim
In these exercises, you will write code to perform molecular dynamics simulations of a harmonic oscillator using both Euler integration and velocity Verlet integration. Through this, you will explore numerical integration methods, energy conservation, and basic thermodynamic averaging.

### The Harmonic Oscillator Model

We will model H<sub>2</sub> as a classical harmonic oscillator. The potential energy for a diatomic molecule modelled as a harmonic oscillator is:

$$U(r) = k(r - r_0)^2$$

where:
- $r$ is the bond length
- $r_0$ is the equilibrium bond length
- $k$ is the force constant

The force can be calculated as:

$$F(r) = -\frac{dU(r)}{dr} = -2k(r - r_{eq})$$

And the acceleration follows from Newton's second law:

$$a(r) = F(r)/m$$

where $m$ is the effective mass of our molecule.

### Exercise 1: Basic Functions

**(a)** Write a function to calculate the potential energy of H₂, modelled as a harmonic oscillator. Use:
- Force constant $k = 575$ N/m
- Equilibrium bond length $r_0 = 0.74$ Å

Plot the potential energy function for bond lengths in the range $0.38$ &#8491; ≤ $r$ ≤ $1.1$ &#8491;.

**(b)** Write a function to calculate the force acting on your system as a function of $r$.
Plot this force function for $0.38$ &#8491; ≤ $r$ ≤ $1.1$ &#8491;.

### Exercise 2: Euler Integration

**(a)** Write code to perform 50,000 steps of molecular dynamics simulation using Euler integration:
- Initial position $r(t=0) = 1.0$ &#8491;
- Initial velocity $v(t=0) = 0.0$
- Mass $m = 0.5$
- Timestep $\Delta t = 1 \times 10^{-5}$
- Store $r(t)$ and $v(t)$ at each step

**(b)** Plot $t$ versus $r(t)$

**(c)** Plot a histogram of the probability distribution of bond lengths, $P(r)$, using `matplotlib.pyplot.hist()`

**(d)** Plot the potential energy, kinetic energy, and total energy of your system as a function of time.

### Exercise 3: Energy Conservation & Velocity Verlet

**(a)** Rerun your simulation for 500,000 steps. Confirm that your simulation is not conserving energy.

**(b)** Rerun your simulation with $\Delta t = 1 \times 10^{-4}$. What happens to your total energy? Why does the energy behave like this?

**(c)** Rewrite your code to use the velocity Verlet algorithm to integrate the equations of motion. Run for 500,000 steps with $\Delta t = 1 \times 10^{-5}$ and confirm that your energy is now conserved.

**(d)** Rerun your simulation using the velocity Verlet algorithm with $\Delta t = 1 \times 10^{-3}$. What happens to your total energy?

