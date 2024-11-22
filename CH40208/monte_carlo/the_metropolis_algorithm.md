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

## Accepting Moves with Probability p

The Metropolis criterion tells us to accept or reject each proposed move according to the following rules:

- If $\Delta E \leq 0$, we always accept the move.
- If $\Delta E > 0$, accept the move with a probability $p = \mathrm{e}^{-\Delta E / kT}$.

## Accepting Moves with Probability p

What exactly does it mean to accept a move &ldquo;with probability $p$&rdquo;? A probability is a number between 0 and 1 that represents the chance of an event occurring. A probability of 0 means the event cannot occur, while 1 means it must occur. Take flipping a fair coin &mdash; if we have no information about how the coin is flipped, we would reasonably assign each outcome a probability 0.5: $p(\text{heads}) = p(\text{tails}) = 0.5$.

In Metropolis Monte Carlo, the probability comes from the Boltzmann factor $p = \exp(-\Delta E/kT)$. For moves that increase the system's energy ($\Delta E > 0$), the Boltzmann factor is a number between 0 and 1. For moves that decrease energy ($\Delta E < 0$), the expression would exceed 1, but we have already decided to accept these moves automatically.

To turn these probabilities into decisions, we use a random number generator. The strategy is straightforward: generate a random number $r$ between 0 and 1, then accept the move if $r \leq p$. This ensures our decisions match the assigned probabilities.

Take our coin flip example where $p(\text{heads}) = 0.5$. We can code this decision as:

```python
is_heads = np.random.rand() <= 0.5
```

The Metropolis algorithm uses the same logic. For a move that increases energy by $\Delta E$:
1. Calculate $p = \exp(-\Delta E/kT)$
2. Generate a random number $r$ between 0 and 1
3. Accept the move if $r \leq p$

Here's what this looks like for a move where $\Delta E = 2kT$:

```python
p = np.exp(-delta_E/kT)  # ≈ 0.135
accept = np.random.rand() <= p
```

In this case, there is about a 13.5% chance of accepting the move. Larger energy increases mean lower acceptance probabilities &mdash; the move becomes less likely but remains possible. This mechanism lets our system occasionally climb uphill in energy while generally favoring lower energy states.

This simple accept/reject rule, guided by physically motivated probabilities, lets us efficiently explore possible states while maintaining the correct Boltzmann distribution.

