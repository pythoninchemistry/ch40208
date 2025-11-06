(sec:geometry-optimisation)=
# Geometry Optimisation 

A common problem in computational chemistry is predicting the equilibrium geometry of a molecule or crystal structure.

In this context, we normally assume that the equilibrium geometry is a single set of atomic positions that **minimises** the total energy of our molecular or crystal. So, how do we find the set of atomic positions that corresponds to a minimum of the total energy?

```{note}
When considering molecular geometries, we need to be careful about how we treat different types of molecular motion:

1. **Translation and rotation**: These motions change the position and orientation of a molecule in space, but do not affect the relative positions of atoms within the molecule. By using internal coordinates (e.g., bond lengths, angles, and dihedral angles) instead of Cartesian coordinates, we can describe molecular geometries independently of their position and orientation in space.

2. **Vibration**: In reality, atoms in molecules are constantly in motion, even at absolute zero (due to zero-point energy). We often either:
   - Ignore vibrational motion entirely, seeking the geometry that minimises potential energy
   - Treat vibrations as harmonic oscillations around equilibrium positions
   
It is worth noting that real molecular vibrations are anharmonic, which means that the average positions of atoms during vibration may not exactly coincide with their equilibrium positions. This leads to subtle differences between observed average bond lengths and calculated equilibrium bond lengths.
```

## Potential Energy Surfaces

Let us start with the simplest possible case: that of a diatomic molecule. For a diatomic molecule, the geometry is completely described by a single parameter: the distance between the two atoms, which we will call $r$. The energy of the molecule as a function of this distance is called the potential energy surface (PES).

In this simple case, our potential energy surface is just a one-dimensional function $U(r)$ that gives us the potential energy for any given internuclear separation $r$. The equilibrium geometry corresponds to the value of $r$ where $U(r)$ reaches its minimum.

This concept of a potential energy surface generalises to more complex systems. For any molecular or crystal system, we can define a function $U(\left\{r\right\})$ that gives us the potential energy for any set of atomic positions $\left\{r\right\}$. Our challenge then becomes:
Given the ability to calculate $U(\left\{r\right\})$ for any set of atomic positions $\left\{r\right\}$, how can we algorithmically find the set of positions that minimises $U(\left\{r\right\})$?
This is fundamentally a mathematical optimisation problem. However, it has several characteristics that make it particularly challenging:
1. The function $U(\{r\})$ is typically not known analytically &mdash; we can only evaluate it at specified points.
2. For all but the simplest systems, we are dealing with many dimensions ($3N-6$ internal coordinates for a molecule with $N$ atoms).
3. The potential energy surface often has multiple local minima, making it crucial to distinguish between local and global minimum energy structures.

For now, we will only focus on point 1 and return to points 2 and 3 later.

