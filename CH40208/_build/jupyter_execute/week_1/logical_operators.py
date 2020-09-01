# Logical operators

**First, run the cell below and watch the video lecture associated with this topic.**

from IPython.display import YouTubeVideo

YouTubeVideo('sarIrXxfuW8', width=560, height=315)

Previously, we used the Jupyter Notebook as a simple calculator. 
However, programs are more useful when we are able to include some *intelligence*, allowing the code to perform different calculations under different circumstances. 
This ability relies heavily on the use of logical operators.

A *logical operator* is a piece of code that returns an object of type *Boolean*, which can be either `True` or `False`. 
The logical operator `==` is one of the most common and translates to *is equal to*, this operator will return `True` if the values on either side are equal, and `False` if they are not. 

# The truth

print(2 - 1 == 1)
print(1 - 1 == 1)

The *is equal to* operator is only one of many logical operators that is available in Python. 

| Description | Mathematical symbol | Pythonic operator | 
|---|---|---|
| is equal to | $=$ | `==` | 
| is less than | $<$ | `<` | 
| is less than or equal to | $\leq$ | `<=` |
| is greater than | $>$ | `>` |
| is greater than or equal to | $\geq$ | `>=` | 
| is not equal to | $\neq$ | `!=` |

> **Short Exercise**
> 
> In the cells below, write code that will return the result of the following logical operations: 
> 
> 1. $1 = 4$
> 2. $10 < 15$
> 3. $3.1415 \neq 3$

# Short Exercise 1



# Short Exercise 2



# Short Exercise 3



## Combining operators

**Run the cell below and watch the video lecture associated with this topic.**

from IPython.display import YouTubeVideo

YouTubeVideo('iMYnAmLI9S0', width=560, height=315)

In addition to the use of individual logical operators, it is possible to use additional keywords to combine multiple operators. 
These keywords are `and` and `or`, which has important *but different* actions:

- The `and` keyword will return `True` if **both** operations are true.
- The `or` keyword will return `False` if **either** operation is true.

We can describe the `and` keyword based on the inputs as follows.

| Input A | Input B | Logic | Output |
|---|---|---|---|
| `True` | `False` | `and` | `False` |
| `True` | `True` | `and` | `True` |
| `False` | `False` | `and` | `False` |

While the descrition of the `or` keyword is given here.

| Input A | Input B | Logic | Output |
|---|---|---|---|
| `True` | `False` | `or` | `True` |
| `True` | `True` | `or` | `True` |
| `False` | `False` | `or` | `False` |

The code below gives an example of the syntax for these operations. 

# Using and and or with electronic spectroscopy selection rules

delta_S = 0
delta_l = +1

orbital_rule = delta_l == 1 or delta_l == -1

delta_S == 0 and orbital_rule

> **Short Exercise**
> 
> Using the `print` function discussed previous, investigate the code above. 
> In the cell below, describe in words what is happening

# your description goes here