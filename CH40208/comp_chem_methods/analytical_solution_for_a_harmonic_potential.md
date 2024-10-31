### Analytical Solution for a Harmonic Potential

To simplify things, we will approximate our diatomic molecule potential energy surface with a harmonic potential of the form

$$U(r) = \frac{k}{2}(r-r_0)^2$$

In this case, we can find the minimum analytically by finding the value of $r$ at which the derivative of $U$ is equal to zero, i.e.

$$\frac{\mathrm{d}U}{\mathrm{d}r} = 0$$

$$\frac{\mathrm{d}U}{\mathrm{d}r} = k(r-r_0) = 0$$

Therefore, at the minimum, $r = r_0$.

This analytical solution if possible because we have a simple mathematical function for $U(r)$. However, for real molecular systems, we typically do not have an analytical form for $U(r)$.

#### Exercise

1. Write a Python function to calculate the potential energy surface for a diatomic molecule with a harmonic bond potential,

$$U(r) = \frac{k}{2}(r-r_0)$$

where $k$ is the bond force constant and $r_0$ is the equilibrium bond length.

Your function should take three arguments as input; $r$, $k$, and $r_0$; and return the potential energy for the input value of $r$.

2. Plot this function for H<sub>2</sub> ($r_0$ = 0.74 &#8491;, $k$ = 575 N m<sup>&minus;1</sup>) for $0.38\leq r \leq 1.1$.

3. Use your function to calculate the potential energy at $r=r_0$. Add a point to your plot at $(U(r_0), r_0)$ and confirm visually that this is the minimum of the potential energy surface.
