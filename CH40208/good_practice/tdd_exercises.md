# Exercise 

The idea for this exercise is to copy and paste the tests and the function definitions into your own Notebook. 
Once the function that your write satifies the test, only `'Test X for Problem Y Passed!'` will be printed when the cell is run. 

```
import numpy as np
```

## Problem 1 

The first function should produce the energy of a photon given a particular wavenumber. Note that the speed of light and Planck's constant are imported from the `scipy.constants` library as `c` and `h` respectively. 
Note, the test wavenumber values are in m<sup>-1</sup>. 

```
from scipy.constants import c, h

def energy(wavenumber):
    return

np.testing.assert_almost_equal(energy(5.03411665e24), 1)
print('Test 1 for Problem 1 Passed!')
np.testing.assert_almost_equal(energy(755117497.6671815), 1.5e-16)
print('Test 2 for Problem 1 Passed!')
np.testing.assert_almost_equal(energy(5.663381232503861e+28), 1.125e4)
print('Test 3 for Problem 1 Passed!')
```

## Problem 2

The second function should be able to determine the volume of a system (assuming the gas is ideal) given the number of moles of gas $n$, the temperature $T$ and the pressure $p$. Again the ideal gas constant is imported for you as `R`.

Remember,

$$pV = nRT$$

```
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, pressure):
    return

np.testing.assert_almost_equal(ideal_gas_law(100, 100, 101325), 0.82057367)
print('Test 1 for Problem 2 Passed!')
np.testing.assert_almost_equal(ideal_gas_law(1, 500, 10132500), 4.10286691e-04)
print('Test 2 for Problem 2 Passed!')
np.testing.assert_raises(ValueError, ideal_gas_law, 1, -1, 10)
print('Test 3 for Problem 2 Passed!')
```

## Problem 3

This function should return the allowed values of the angular momentum quantum number $l$, given a particular principal quantum number $n$.

Remember,

$$ 0 \le l \le n - 1 $$

```
def allowed_angular_momentum_quantum_numbers(principal_quantum_number):
    return 

np.testing.assert_equal(allowed_angular_momentum_quantum_numbers(3), [0, 1, 2])
print('Test 1 for Problem 3 Passed!')
np.testing.assert_equal(allowed_angular_momentum_quantum_numbers(6), [0, 1, 2, 3, 4, 5])
print('Test 2 for Problem 3 Passed!')
np.testing.assert_raises(ValueError, allowed_angular_momentum_quantum_numbers, 0)
print('Test 3 for Problem 3 Passed!')
np.testing.assert_raises(TypeError, allowed_angular_momentum_quantum_numbers, 1.5)
print('Test 4 for Problem 3 Passed!')
```

## Problem 4

This function should return the rate constants $k$ for a reaction with a given activation energy $E_a$ and pre-exponential factor $A$, and at a range of temperatures $T$.

Remember,

$$ k = A \exp{\frac{-E_a}{RT}} $$

```
def arrhenius_equation(pre_exponential_factor, activation_energy, temperature):
    return

np.testing.assert_almost_equal(arrhenius_equation(23e10, 24131, 300), 14461992.1514407)
print('Test 1 for Problem 4 Passed!')
np.testing.assert_almost_equal(arrhenius_equation(29, 10, np.array([6, 26, 226])), 
                               [23.73241504, 27.68905521, 28.8460781])
print('Test 2 for Problem 4 Passed!')
```

## Problem 5

Write a function to calculate the energy of a Morse potential (this potential is a good model of a chemical bond) at a given set of distances. The functional form of a Morse potential is,

$$E(r) = D_e\{1-\exp{[-(r-r_e)]}\}^2 $$

where $D_e$ is the dissociation energy, $r$ is the bond length, and $r_e$ is the equilibrium bond length.

```
def morse(dissociation_energy, r, r_e):
    return 
    
np.testing.assert_almost_equal(morse(4.52, np.linspace(0.5, 1, 10), 0.74), 
                               [0.332564 , 0.1854401, 0.0855355, 0.0261688, 
                                0.0014542, 0.0062124, 0.0358916, 0.0864975, 
                                0.1545298, 0.2369265])
print('Test 1 for Problem 5 Passed!')
np.testing.assert_almost_equal(morse(0.59, 5, 1.5), 0.5549050979213414)
print('Test 2 for Problem 5 Passed!')
```
