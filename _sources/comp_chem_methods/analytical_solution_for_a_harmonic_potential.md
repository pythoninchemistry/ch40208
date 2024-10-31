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

````{note}
Your instinct is probably to work in SI units, in which case your harmonic potential function will return energies in joules. Because you are calculating the potential energy of a single H<sub>2</sub> molecule, working in joules will give very small numbers: for example, doubling the bond length gives a potential energy increase of only 1.57 &times; 10<sup>&minus;18</sup> J. Working with such small numbers can cause problems for some numerical optimisation methods, because any change in bond-length gives a change in potential energy that is very small, and can be considered so close to zero that the optimisation algorithm decides that convergence has been reached, and stops prematurely.

You can make your code much more numerically robust by working in more suitable energy units, such as electronvolts (eV). In these units, the same doubling of the H<sub>2</sub> bond length gives an energy increase of approximately 9.8 eV, which is much easier for numerical algorithms to work with.

The conversion factor from joules to electronvolts is available as part of the `scipy.constants` module:

```python
from scipy.constants import physical_constants

joules_to_ev = 1 / physical_constants['electron volt'][0]

energy_in_eV = energy_in_joules * joules_to_eV
```
````

2. Plot this function for H<sub>2</sub> ($r_0$ = 0.74 &#8491;, $k$ = 575 N m<sup>&minus;1</sup>) for $0.38\leq r \leq 1.1$.

3. Use your function to calculate the potential energy at $r=r_0$. Add a point to your plot at $(U(r_0), r_0)$ and confirm visually that this is the minimum of the potential energy surface.
