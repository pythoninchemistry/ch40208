# Exercise 2

In this exercise, we will design code to calculate the equilibrium constant, $K$, from the following equation,

$$ K = \exp\bigg(\frac{\Delta G}{RT}\bigg) $$, 

where $R = 8.314$ JK<sup>-1</sup>mol<sup>-1</sup>, $\Delta G$ is the free energy change, and $T$ is the temperature. 

You code should be able to handle values of the free energy change in any of kJmol<sup>-1</sup>, Jmol<sup>-1</sup> or eV (where $1$ eV = $96485$ Jmol<sup>-1</sup>).
The unit of the temperature is only going to be K.

Again, this notebook is structured to help you understand how the problem should be broken down.

First, we need to have the definition of the temperature, value of $\Delta G$ and the units that are being used. 

# create a variable for each of the temperature, the free energy change value and associated unit



If it unit is Jmol<sup>-1</sup>, no change is necessary to the value (as this agrees with the unit of $R$). Therefore this will be our `else`, but we need to perform a unit conversion `if` the unit is kJmol<sup>-1</sup> (a multiplication by 1000) of `elif` the unit is eV (a multiplication by 96485). 

# Using if, elif, and else convert the free energy value to J/mol



Now that the value is in the correct units, we need to perform the arithmetic. 

However, you should be aware that Python does not natively support an exponential function. 
This means that we will have to `import` the function from a library (this will be discussed in detail in future weeks). 
Please make sure that the cell below is run, or else the code will not work. 

# importing the exp function 
from math import exp

The `exp` function is used by putting the value that you want to take the exponential of within brakcet immediately following the `exp`. 
For example, to calculate the exponential of 2, the code would be `exp(2)`. 

# Do the arithmatic in this cell, using the exp function



Finally, print the result (use a formatted string to make the result clear). 

# print here



Now, go back and modify your `if`, `elif`, and `else` statements so that a string is printed warning the user of an unphysical temperature (e.g. less than or equal to zero). 