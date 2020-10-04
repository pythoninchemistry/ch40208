# Print statements

## Displaying data

Until now, we have been using the built-in functionality of the Jupyter Notebook to display data on the screen.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F6d1q87iYba.png?alt=media&token=6fb5c325-8986-4dfc-a96a-fb45f7d9bd3e)

**Code blocks** are not limited to single lines of code&mdash;this would make working in Jupyter Notebooks extremely tedious when writing more complicated programs. 

But what happens if we run a cell that contains more than one statement?

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FU3NR07xlwM.png?alt=media&token=12897531-b40f-4a82-ad67-39dca83b695f)

Only the output from the **last** statement is displayed as the cell output. The first two statements have been executed when we run the cell, but no output is displayed.

The default setting for Jupyter Notebooks is to only display the output from the final statement in any code cell. While it is possible to [change this setting](https://stackoverflow.com/questions/36786722/how-to-display-full-output-in-jupyter-not-only-last-result) so that all the output is displayed, the usual way to control what is displayed is to use the `print` **function**.

## A brief intro to functions

A **function** is a piece of reusable code that takes zero or more inputs, performs a specific computation, and **returns** an output. 

To use a function (known as **calling** the function) we type the function name, followed by a pair of brackets. Anything inside the brackets specifies the inputs to the function. These inputs are called **arguments**, and are said to be **passed** to the function:

```python
print("Hello World!")
```

Here, we are calling the `print` function with one argument; the **string** `"Hello World!`. 

If we run this in a **code cell**, the string is printed:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F78cWkzJ9yI.png?alt=media&token=6d80ff9a-7e6e-43ea-b1e3-9612d0e4de69)

Returning to our previous example, the following set of print statements displays all three strings:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FT786f2Vgia.png?alt=media&token=20fdca16-469e-4c02-a6a4-08f7bd04ce81)

You might have spotted that these examples using `print` do not give an `Out [ ]:` output under the code cell.

Remember that a **function** is a piece of code that returns an output. So what is the output returned by `print`? 🤔

Somewhat confusingly, `print` returns `None`. `None` is a **null object** that represents no data.

Remember that when you run a code cell, whatever data is produced by the final statement in that cell is displayed as the **cell output** after `Out [ ]:`.

But calling `print` returns `None`. The examples above produce **no data**, and so there is nothing to display as the **cell output**.

<p align="center">
    <img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FSS2_oGj9Sp.png?alt=media&token=c7542ed7-1d4f-48f4-a804-980677edc0ef" width="50%" />
</p>

If zero **arguments** are passed to an **function**, the **function** is still **called** by writing the function name followed by a pair of brackets. e.g.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FQ2thbkGKv6.png?alt=media&token=b6d50780-2109-4d6f-9637-a3cd0ec6fa58)

**Calling** `print` with no arguments prints a blank line (and returns `None`, so no cell output is displayed).

Writing a function name __without__ the following brackets is still valid Python. But instead of **calling** the function, and performing whatever computation you expected, you are simply referring to the data that represents that function. e.g.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FBTocyIH_qH.png?alt=media&token=5205b8dc-1b32-41bf-9ace-4bfe75580a90)

Now the cell output shows a string representation of the data produced by the final statement; in this case this is the `print` function itself.

## Slightly more complex print statements

The `print` function can also be passed more than one argument. `print` will try to convert each argument to a string and then **concatenate** these into a single output, e.g.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FQtqxmcuZsV.png?alt=media&token=07677f56-686d-4484-88c4-64c4f03291f0)
