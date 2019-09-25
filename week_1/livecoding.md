# Living Coding Help Sheet

## Week 1: Introduction to Python

### Demo 1 - Jupyter

This is a demonstration of how to launch and operate a Jupyter Notebook:

- Launch Jupyter Notebook on BUCS machine.
- Create directory `CH40208` to be used for the course, also create subdirectory for `week 1` as an example.
- Open an empty Notebook and show how code may be written and run.
- Show how Markdown can be written in a Notebook cell and explain the importance of *documenting* your work.
- Give the route to download anaconda Python and therefore the Jupyter Notebook on home computers/laptops.

### Demo 2 - Variables

One example of each of the intrinsic variable types, can use `type()` to identify.

```
42
type(42)
```

```
3.14
type(3.14)
```

```
4+1j
type(4+1j)
```

```
'hello world'
type('hello world')
```

```
True
type(True)
```

Instead of writing a variable out, we can assign it to a value.

```
pi = 3.14
pi
```

The value 3.14 will is now stored in the variable name `pi`, therefore `pi` has the type `float`.

```
type(pi)
```

Not limited to floats.

```
message = 'Chemistry is cool B-)'
type(message), message
```

### Demo 3 - Arithmetic

Python can to maths.

```
2 + 2
```

```
6 * 4
```

```
2 ** 8
```

Brackets are important and BODMAS is used.

```
2 * 3 + 4
```

```
2 * (3 + 4)
```

### Demo 4 - Mixed Mode Operations

Show that Python promotes types.

```
type(1 + 5.3)
```

```
type(9.8 * (3 + 1j))
```

```
9.3 + 'hello'
```

Briefly cover how to understand the resultant error from the above.

The following will promote the two ints to floats.

```
3 / 2
```

But `//` will always round down and return an int.

```
3 // 2
```

### Demo 5 - Output and Input

How to print.

```
print('Hello World!')
```

Printing numbers, generally we can do the following.

```
print('This is the number: {}'.format(3))
```

However this can become ugly for floating point numbers.

```
print('This is ugly: {}'.format(23 / 7))
```

Let reduce the number of decimal points.

```
print('This is prettier: {:.2f}'.format(23 / 7))
```

We can also read information in for the user.

```
name = input('What is your name? ')
```

This will store the string as the variable `name`.

```
print(name)
```

Note that this understands everything as a string, so if we want a number it must be converted manually.

```
age = int(input("How old are you? "))
```

```
print(age)
```

```
print(type(age))
```

Similar can be done with `float()` and `complex()`.

### Demo 6 - Logical operators

Python will return either `True` or `False` to a series of logical operations.

```
1 < 2
```

```
5 == 10 - 5
```

```
7 != 7
```

Note that these are Boolean variables that are returned.

```
fact = 3 == 3
```

```
print(fact)
```

```
print(type(fact))
```

### Demo 7 - Flow control

If and else functions can be used.

```
a = 4
if a < 4:
    print('a is less than 4')
else:
    print('a is 4 or more')
```

Run this again with a new value of 4.

```
a = 4
if a < 4:
    print('a is less than 4')
elif a == 4:
    print('a is 4')
else:
    print('a is more than 4')
```

### Demo 8 - Compound logic

It is possible to compound the logical operators using AND and OR.

```
a = 3
b = 5
if (a < 4) and (b > 4):
    print('a and b cannot be the same value')
else:
    print('a and b might be the same value')
```

```
a = 4
b = 4
if (a < 4) or (b > 4):
    print('Either a is less than 4 OR b is more than 4')
else:
    print('Either a is more than 3 OR b is less than 5, or both')
```
