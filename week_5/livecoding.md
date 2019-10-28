# live coding - week 2

## demo 1

Write the pH function out in a module

```
import numpy as np

def pH(conc_h):
    """Determine the pH for a given H+ concentration

    Parameters:
        conc_h (float): Concentration of H+ (or H3O+) 
                        in solution

    Returns:
        float: The pH value
    """
    return np.log10(conc_h)
```

Then show the `?` functionality in Jupyter

## demo 2

Create a seperate module (q_module.py)

```
import numpy as np

def electron_accommodation(n):
    if not isinstance(n, int):
        raise TypeError('The principal quantum number (n) must be an integer')
    if n <= 0:
        raise ValueError('The principal quantum number (n) must be greater than 0')
    return 2 * n ** 2
```

then in a notebook the following

```
import numpy as np

np.testing.assert_almost_equal(q_module.electron_accomodation(1), 2)
print('Test 1 passes')
np.testing.assert_raises(TypeError, q_module.electron_accomodation, 1.2)
print('Test 2 passes')
np.testing.assert_raises(ValueError, q_module.electron_accomodation, -5)
print('Test 3 passes')
np.testing.assert_almost_equal(q_module.electron_accomodation(2), 6)
print('Test 4 passes')
```

The bottom test will fail

```
4 * n - 2
```