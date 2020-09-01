# Print statements

**First, run the cell below and watch the video lecture associated with this topic.**

from IPython.display import YouTubeVideo

YouTubeVideo('KLTleMeNkU8', width=560, height=315)

Until now, we have been using the built-in functionality of the Jupyter Notebook to "print" information from our code. 
You may have noticed that the result of the final line in a given Juypter cell will be printed below it. 

to_print = "Like how this is printed"

to_print

However, if you would like to get information from other lines in the cell (or from within a larger program or function, as we will see in later weeks), it is necessary to be able to *print* from the code. 
This is where the *print statement* comes in, which in Python looks like this.

# Print Hello World!

print("Hello World!")

This will output the string `Hello World!` when the cell is run (some of you may be aware that printing "Hello World!" is considered a right of passage in programming and is often the first thing someone will learn to do in a new programming language). 

Any of the [types](variable_types.ipynb) discussed previously may be printed with the print statement.
Additionally it is also possible to use the print statement to insert numerical values into a string. 
We can even prescribe how the number is written, for example, in the code below the information bewteen the curly brackets defines that the floating point number (`f`) should be written with two (`2`) numbers following the decimal point (`.`). 

# More interesting printing

pi = 3.1415

print("pi is approximately {}".format(pi))
print("pi to 2 decimal places is {:.2f}".format(pi))

More inforamtion about the `format` command can be found [online](https://www.w3schools.com/python/ref_string_format.asp).