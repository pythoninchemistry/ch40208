## The Metropolis Algorithm

The Metropolis algorithm provides an elegant solution to this sampling problems. Rather than trying to calculate absolute probabilities, it works with probability ratios:

Starting from a configuration $i$:
1. Propose a random move to configuration $j$.
2. Calculate the energy change $\Delta E_{ij} = E_j - E_i$.
3. Accept the move with probability:

$$A(i \rightarrow j) = \min(1, \exp(-\Delta E_{ij}/kT))$$

This acceptance criterion ensures:
- Moves that lower energy ($\Delta E < 0$) are always accepted.
- Moves that raise energy are accepted with probability $\exp(-\Delta E/kT)$
- The partition function $Z$ cancels out in the ratio

