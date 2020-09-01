# Arithmetic

Let's now look at how we can use the *numerical* variable types. 
Python and the Jupyter Notebook are able to perform simple mathematical operations *natively*. 
Most powerful mathematical operations are discussed [later](../working_with_data/numpy_arrays/). 

The operations that Python can perform natively include, 

| Operation | Mathematical notation | Pythonic notation |
|---|---|---|
| Addition | $ a + b $ | `a + b` |
| Subtraction |  $ a - b $ | `a - b` |
| Multiplication | $ a \times b $ | `a * b` |
| Division | $ a \div b $ | `a / b` |
| Exponent | $ a ^ b $ | `a ** b` |

Beware that the multiplication in Python is explicit, while in mathematics you could write $1.5nRT$ to indicate $0.5 \times n \times R \times T$, in Python all of the previous implicit multiplication must be included. 
So in Python we would have `1.5 * n * R * T`. 

With these basic tools alone, and the ability to assign variables, it is possible to use the Jupyter Notebook as a simple calculator. 
For example, we could assign some values to the variables `n`, `R`, and `T`, and calculate the internal energy of a monatomic ideal gas. 

```python
n = 1
R = 8.314
T = 300

1.5 * n * R * T
```

## Order of operations

A single line of code can include a series of different arithmetic operations. 
Therefore, it is necessary to follow a hierarchy, also known as the *order of operations*. 
Python follows the order of operations that should be familiar from mathematics, you may know this as [BODMAS](https://en.wikipedia.org/wiki/Order_of_operations):

- **B**rackets
- **O**rder
- **D**ivision
- **M**ultiplication
- **A**ddition
- **S**ubtraction

> **Exercise**: Without using the computer or a calculator, and following the BODMAS order of operations, calculate the following:
> 1. $24 \div (10 + 2)$
> 2. $5 + 16 \div 2 \times 3$
> 3. $[32 \div (6 + 2)] ^ 2$
> 
> Now check that your answers match the result that Python produces using a Jupyter Notebook.

## Mixed-type operations

When the two operands, $4$ and $3$ in the code `4 + 3`, are of the same type, the result of some arithmetic operations will typically also be of this type. 
For example, below the two floats produce a float, 

```python
type(4.3 + 2.5)
```

However, where the operations is on operands of different types, it is necessary to modify one of them before the operation can be performed. 
For example, below an integer is multiplied by a float, which results in an object of type `float`. 

```python
type(2 * 4.0)
```

This is because, Python is automatically converted the type of `2` before the operation. 
If you could see all of the steps of the multiplication, it would look like this,
```
>> 2 * 4.0
>> 2.0 * 4.0
>> 6.0
```

In Python 3 (the version of Python that we are working with), if one integer is divided by another, then both are converted to floats first. 
So in the code below, the variable `both_int` is a float with the value `0.5`.

```python
both_int = 2 / 4
both_int, type(both_int)
```

In the older Python 2, this would have returned an integer with a value of `0`, as the number is rounded down. 
However, with Python 3, the operator `//` (known as floor division, because it rounds down) would be required to achieve this result. 

```python
floor_division = 2 // 4
floor_division, type(floor_division)
```
