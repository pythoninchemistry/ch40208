# Variables

**First, run the cell below and watch the video lecture associated with this topic.**

from IPython.display import YouTubeVideo

YouTubeVideo('zjVhOQ14sBE', width=560, height=315)

A *variable* is a container that a Python uses to store some data.
The variable can be created and reused at a later stage in the code. 
In the cell below, assign the value `1` to the variable `principal_quantum_number`.

# Variable assignment 



Not all variables are the same, they may have different *types*. 
Different operations are possible depending on the variable type. 
Variable types that are present in Python include: 

- *integers* (`int`): these are whole numbers (1, 2, 0, -3, etc.); there is no decimal point and they can be positive, negative, or zero. 
- *floats* (`float`): these are all real numbers (1.0, 3.14, 0.0, -6.28); any value that can be described with a decimal point. This includes numbers in scientific notation, which are written `6.02e23`, where the `eXX` takes the place of the $\times10^{\text{XX}}$. 
- *complex* (`complex`): these are complex numbers, which should be familiar from mathematics, such as $1 + 2i$. However, in Python, a `j` is used instead of the $i$. 
- *string* (`str`): a string is a textual variable, such as a word or a sentence; these are written between single or double inverted commas, `'like this'` or `"this"`.
- *boolean* (`bool`): named for [George Boole](https://en.wikipedia.org/wiki/George_Boole), who defined an algebraic logic system in the 19th century; a Boolean is a *logical* valiable type that may hold one of two values, either `True` or `False`. We will come back to *logic* later.

In the cells below, try and define a *chemistry* example for one of each of the four variable types mentioned above (and don't just copy those from the video!).

> **Note**: `str` objects are contained within either double or single quotes. 
However, you **cannot** use a mixture of the two. e.g. `my_string = 'Hello World!"` will return an error.

# Define a int



# Define a float



# Define a string



# Define a boolean



The `type()` function will inform you of the type of the variable that is passed as an argument, complete the cells below such that they return the appropriate type. 

# Return a string

a_string = 
type(a_string)

# Return a float

a_float = 
type(a_float)

# Return a int

a_int = 
type(a_int)

> **Short Exercise**
> 
> Using the cell below, consider the difference in *type* between `1`, `1.` and `1.0` as interperated by Python. 

# The difference in 1

