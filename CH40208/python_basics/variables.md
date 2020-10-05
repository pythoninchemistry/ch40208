# Variables

Until now, all of the Python examples have used explicit data values typed directly into the **code cells**. This is okay for typing out a quick numerical calculation, but does not let us do anything any more sophisticated with our data. To do anything more complex your code will need to store and retrieve data, and to change the values of these data as you perform your calculations, which we do using **variables**.

## What is a variable?

A variable is a Python is an object that stores some data. 

This data can be a wide range of **types**, including `int`, `float`, or `complex`; a `string`; a `bool`; even a function, or a **collection** of other variables. 

## Assigning a variable

To create a new variable and **assign** it a value we use `=`.

```
days_in_october = 31
```

This creates a variable named `days_in_october` and assigns it the integer value `31`. 

<p align="center">
    <img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fa6JgzoVeFq.png?alt=media&token=a005e60b-a5a0-42a8-a57d-2d02e7c5fc1d" width="32%" />
</p>

The left-hand side of the assignment expression is the **variable name**. 
- Variable name must start with a letter or an underscore.
- Variable names can be any length and can contain upper- and lower-case letters, numbers, and underscores.
- Variable names are **case sensitive**. `my_name` and `My_Name` are two different variables.
- Variable names cannot be special **reserved keywords**. You can see the full list of **reserved keywords** by running the command `help("keywords")` in a **code cell**.

Now we can use the variable `days_in_october` in place of the integer `31`:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F5a1IjNuv90.png?alt=media&token=eb858444-a256-4723-9804-24f16aa7c4c6)

### aside: f-strings

A neater way to do this is to use **f-strings**, which provide a way to embed expressions inside strings. An **f-string** is a **string literal** with an `f` character at the beginning, and curly brackets enclosing any expressions. When the **f-string** is created, any enclosed expressions are evaluated to give a single **interpolated** string:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FvwPHubLqtf.png?alt=media&token=38254aab-a9dd-4ca1-8426-bcee67b5dec6)

`days_in_october` can be used in any of the ways that we might use the value assigned to it. i.e. `days_in_october` behaves like an **integer**. If we call type with `days_in_october` we can confirm the assigned value is an `int`. 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F-ad776-SGA.png?alt=media&token=d01ffa6f-01b9-42d8-a5fe-a407243822bb)

Variables can also appear on the right-hand side of variable assignments.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fj93ImUGW5v.png?alt=media&token=0f34ff15-c380-4d44-860a-5bae7806b8b3)

- In the first line, we create a variable `a` and assign it the value `3`.
- In the second line, we create a variable `b` and assign it to the same value as the variable `a`. This is the same as if we had written `b = 3`.
- In the third line we print `b`.

<p align="center">
    <img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FvVo9nrs0yZ.png?alt=media&token=77d56d32-574b-4bf1-bd2a-bf41c09a1a0b" width="30%" />
</p>

Because `b` is assigned to the **value** stored in `a`, and not to `a` itself, if we **reassign** `a`, the value stored in `b` does not change.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FBh8Rmkvzww.png?alt=media&token=602398c3-251a-4d40-b786-a4afbd46d5bb)

<p align="center">
    <img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fs1JfhRYRHR.png?alt=media&token=18c052f7-76e1-48bc-9ac7-861903d6fd3d" width="50%" />
</p>

## Multiple assignment

Python allows multiple variables to be assigned in the same statement:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F9Oq6l6l3au.png?alt=media&token=f9f20547-0042-4b2d-8f82-462cc23b0050)

## Empty variables

A variable may also be set to contain no value by assigning it `None`.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FXy-esPUMZ0.png?alt=media&token=34d067d6-07fd-4b26-b1cb-c1cee449755f)

