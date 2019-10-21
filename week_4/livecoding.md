# live coding - week 2

## demo 1

```
a = 'hello'
b = 2

a + b
```
 
This produces a different Error from 

```
b + a
```

## demo 2

IndexError

```
a = [1, 3, 5]

print(a[3])
```

ModuleNotFoundError

```
import nmupy
```

TypeError is that above

ValueError

```
a = float('banana')
```

NameError

```
b = 3.14
print(c)
```

ZeroDivisionError

```
a = 12 / 0 
print(a)
```

## demo 3

```
import numpy as np

a = np.linspace(1, 9, 9)

a = np.reshape(a, (3, 3))

print(a)
print(np.mean(a, axis=2))
```

Then google the error message

### demo 4 

```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 10)
y = np.linspace(1, 10, 9)

plt.plot(x, y)
plt.show()
```

Don't be scared

## demo 5 

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

Then in notebook run

```
import q_module

q_module.electron_accommodation(2)

q_module.electron_accommodation(-12)

q_module.electron_accommodation(1.23)
```

When an error is thrown show traceback logic

## demo 6 

Show the visualisation library usage 

