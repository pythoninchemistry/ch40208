# Living Coding Help Sheet

## Week 2: Loops, lists, arrays, optimisation, and plotting

### Demo 0 -  Review last Week

Remind students about the following:
- Variable types
- Arithmetic
- Output/Input
- Logical operators and compound operations
- Flow control

### Demo 1 - Lists

Lists need [ ]

```
shopping = ['banana', 'avocado', 'bread']
```

```
print(shopping)
```

```
print(shopping[0])
```

```
print(shopping[-1])
```

```
shopping[1] = 'rice'
```

```
print(shopping)
```

```
print(shopping[1:])
```

```
me = ['Drew', 182.7, 72]
```

```
print(me)
```

```
me.append('Oxford')
```

```
print(me)
```

```
del me[2]
```

```
print(me)
```

```
ben1 = ['Ben', 'Bath']
```

```
ben2 = [178.4, 75]
```

```
ben = ben1 + ben2
```

```
print(ben)
```

### Demo 2 - Loops

```
shopping = ['banana', 'avocado', 'bread']
for item in shopping:
    print(shopping)
```

```
i = 0
while i < 10:
    print(i)
    i = i + 1
```

```
for i in range(0, 10):
    print(i)
```

```
sum_not_four = 0
for i in range(0, 5):
    if i == 4:
        continue
    sum_not_four = sum_not_four + i
print(sum_not_four)
```

```
sum_not_four = 0
for i in range(0, 5):
    if sum_not_four > 6:
        break
    sum_not_four = sum_not_four + i
print(sum_not_four)
```

### Demo 3 - Importing libraries

```
import numpy as np
```

```
from numpy import pi
```

### Demo 4 - Numpy arrays

```
my_array = np.array([73, 52, 93, 77, 60, 88])
print(my_array)
```

```
print(np.sum(my_array))
print(np.mean(my_array))
print(np.std(my_array))
```


### Demo 5 - Code optimisation

```
a = np.linspace(0, 10000)
ssq = 0
for i in a:
    ssq += np.sqrt(i)
print(ssq)
```

```
ssq = np.sum(np.sqrt(a))
print(ssq)
```

### Demo 6 - Duplication

```
my_shopping = ['banana', 'avocado', 'bread']
print(my_shopping)
your_shopping = my_shopping
your_shopping[0] = 'apple'
print(your_shopping)
print(my_shopping)
```

```
my_shopping = ['banana', 'avocado', 'bread']
print(my_shopping)
your_shopping = copy(my_shopping)
your_shopping[0] = 'apple'
print(your_shopping)
print(my_shopping)
```

### Demo 7 - Plotting

This is data for the conversion of cyclopropane to propene

```
t = np.array([0, 300, 600, 900])
c = np.array([0.099, 0.079, 0.065, 0.054])
```

```
import matplotlib.pyplot as plt

plt.plot(t, c)
plt.xlabel('Time/s')
plt.ylabel('[C3H6]/M')
plt.show()
```

```
plt.plot(t, np.log(c))
plt.xlabel('Time/s')
plt.ylabel('ln([C3H6])/M')
plt.show()
```

### Demo 8 - Reading data with np.loadtxt

Import data of IR spectra for benzoic acid

Open text file and show the students

```
import numpy as np

wavenumber, transmittance = np.loadtxt('benzoic_acid.txt')
plt.plot(wavenumber, transmittance)
plt.xlabel('Wavenumber/cm$^{-1}$')
plt.ylabel('Transmittance')
plt.show()
```

```
import numpy as np

wavenumber, transmittance = np.loadtxt('benzoic_acid.csv', delmiter=',')
plt.plot(wavenumber, transmittance)
plt.xlabel('Wavenumber/cm$^{-1}$')
plt.ylabel('Transmittance')
plt.show()
```
