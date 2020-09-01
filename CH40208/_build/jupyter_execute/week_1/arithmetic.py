# Arithmetic

**First, run the cell below and watch the video lecture associated with this topic.**

from IPython.display import YouTubeVideo

YouTubeVideo('TP0VoPQ2qbw', width=560, height=315)

Python and the Jupyter Notebook is able to perfomr simple mathematical operations natively, examples of the operations are given below. 

| Operation | Mathematical notation | Pythonic notation |
|---|---|---|
| Addition | $ a + b $ | `a + b` |
| Subtraction |  $ a - b $ | `a - b` |
| Multiplication | $ a \times b $ | `a * b` |
| Division | $ a \div b $ | `a / b` |
| Exponent | $ a ^ b $ | `a ** b` |

Using this basic tools alone, it is possible to use a Jupyter Notebook as a rudimentary calculator.

> **Note**: multiplication in Python is *explicit*, if you want to multiply $a$ and $b$, `ab` will not work.
> You need to write `a * b`. 

# A simple sum

2 + 4

## Order of operations

A single line of code can include a series of the arithmetic operations outlined above. 
Therefore, it is necessary to follow a hierarchy, also known as the *order of operations*. 
Python follows the order of operations that should be familiar from mathematics, you may know this as BODMAS: 

- **B**rackets
- **O**rder
- **D**ivision
- **M**ultiplication
- **A**ddition
- **S**ubtraction

> **Short Exercise**
> 
> Without using the computer, and following the BODMAS order of operations calculate the following:
> 1. $ 24 \div (10 + 2) $
> 2. $ 5 + 16 \div 2 \times 3 $
> 3. $ (32 \div (6 + 2))^2 $
>
> Now check that your answers match the result that Python produces in the cell below.

# Check your maths here



## Mixed type operations

When the two operands (`4` and `3` in the code `4 + 3`) are of the same type, the result of some arthimetic operation will typically also be of this type. 

# The type doesn't change 

type(4.3 + 2.5)

However, where the operation is on two operands of different types, it is necessary to modify one of them *before* the operation is performed. 
For example, consider the code below, where an `int` is multiplied by a `float`, which results in an object of type `float`. 

type(2 * 4.0)

This is because the `2` is converted to a `float`, such that the operation is effectively `2.0 * 4.0`.

In Python 3, is one `int` is divide by another `int`, then both are converted to `float` objects first. 
So in the code below, the variable `both_int` will be a float with the value `0.5`. 

# integer division

both_int = 2 / 4

type(both_int)

In the older Python 2, this would have returned an `int` with a value of `0`. 
However, with Python 3, the operator `//` (known as floor division) would be required to achieve this result. 

# floor division in action

floor_division = 2 // 4

floor_division, type(floor_division)