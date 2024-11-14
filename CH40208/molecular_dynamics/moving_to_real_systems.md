## Moving to Real Systems

### Modelling More Than One Atom

Real molecular dynamics simulations deal with far more complexity than our simple examples suggest. Instead of single particles, we simulate systems with multiple atoms moving in three dimensions. This means our positions, velocities, and forces become vectors in a $3N$-dimensional phase space. The velocity Verlet equations take on vector form:

$$\vec{r}(t + \Delta t) = \vec{r}(t) + \vec{v}(t)\Delta t + \frac{1}{2}\vec{a}(t)\Delta t^2$$

$$\vec{a}(t + \Delta t) = \frac{1}{m}\vec{F}(t + \Delta t)$$

$$\vec{v}(t + \Delta t) = \vec{v}(t) + \frac{1}{2}[\vec{a}(t) + \vec{a}(t + \Delta t)]\Delta t$$

### The Ergodic Hypothesis

To calculate thermodynamic properties from these simulations, we rely on the **ergodic hypothesis**, which states that the time average of a property equals its ensemble average. This means we can calculate equilibrium properties by averaging over a sufficiently long simulation time. This assumption is not always valid, however, particularly for systems with high energy barriers between different states.
