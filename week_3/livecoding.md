# live coding - week 3

## demo 1

show and run worked examples (show how to download and access)

## demo 2 - function

```
def hello_world():
    """
    Prints hello world!
    """
    print('hello world')
```

```
def square_root(x):
    """
    More readable sqrt
    """
    return np.sqrt(x)
```

## demo 3 - functions arguments

```
from scipy import constants 

def kinetic_energy(temperature, molecules=True):
    """
    Capable of evaluating the kinetic energy of 
    molecules and moles of molecules
    """"
    if molecules:
        return constants.k * temperature
    else:
        return constants.R * temperature
```

```
def sum_of_squared(a, *b):
    """
    Sum the squares of many things
    """
    result = a ** 2
    for i in b:
        result += i ** 2
    return result
```

## demo 4 - modules

Note that this is deliberately from the handout (will be helpful in the problem

In an atom_helper.py file add the following

```
import numpy as np

def distance(a, b)
    """
    Determined the distances between two points, 
    in any number of dimensions
    """
    return np.sqrt(np.sum(np.square(a - b)))
```

Point out that np.square == ** 2

Show the use of this function in a notebook 

```
import numpy as np 
import atom_helper

atom1 = np.array([1, 4, 2]) 
atom2 = np.array([5, 2, 6])

dist = atom_helper.distance(atom1, atom2) 

print(dist)
```

## WHILE THEY WORK

Write the code to plot the e, e', and e'' 

then show this in the explanation of way NR isn't good at times

## demo 5 - scipy optimise minimise

```
import numpy as np

def energy(r, A, B):
    """
    The Lennard-Jones potential
    """
    return A / np.power(r, 12) - B / np.power(r, 6)

from scipy.optimize import minimize

initial_guess = 4

results = minimize(energy, initial_guess, args=(1e5, 40)) 

print(results)
```

CHECK IF THIS WORKS FOR *args before if so use this

## demo 6 - global optimisation 


