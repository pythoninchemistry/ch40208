# Investigation of the ideal gas law

A large ballon is filled with argon gas, the temperature is then varied and the volume and pressure is measured. 
The results of this are shown in the table below.

| Temperature/K | Volume/m<sup>3</sup> | Pressure/Pa |
|---|---|---|
| 200 | 0.8 | 5020 |
| 600 | 0.2 | 60370 |
| 1000 | 1.0 | 20110 |
| 1400 | 0.6 | 46940 |
| 1800 | 0.1 | 362160 |

We will assume that the argon gas will follow the ideal gas law, which states, 

$$ pV = nRT, $$ 

where, $p$ is the pressure, $V$ is the volume, $n$ is the number of moles of gas, $R$ is the [ideal gas constant](https://en.wikipedia.org/wiki/Gas_constant), and $T$ is the temperature.
Carry out the following: 

- Plot the relationship between $p$ and $T$.
- Plot the relationship between $V$ and $T$.
- Plot the relationship between $pV$ and $T$.
- For each data point calculate the value of $n$, the number of moles of argon in the ballon, and store these values in a NumPy array.
- Find the mean and standard error of this array (the standard error is the [square root](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html) of the standard deviation) and print these values in a string using the [f-strings](https://pythoninchemistry.org/ch40208/python_basics/variables.html#aside-f-strings) syntax.

## Tip 

The ideal gas law can be imported from the SciPy package and stored as the variable `R` with the following code:

```
from scipy.constants import R
```