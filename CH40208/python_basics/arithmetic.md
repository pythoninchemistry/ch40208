# Arithmetic

## Using variables in mathematical expressions

The ability to assign data to variables and then to use these variables as references back to the data allows the construction of infinitely more complex calculations than the simple single-line expressions we saw previously.

As a relatively simple example, assigning numerical data to variables allows us to express mathematical calculations algebraically.

## Example: the quadratic formula

The [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula) is an expression for solving a quadratic equation of the form

$$ax^2+bx+c = 0$$

where $x$ is the unknown value we want to find, and $a$, $b$, and $c$ are fixed parameters.

The formula to find the solutions $x$ is:

$$x = \frac{-b\pm \sqrt{b^2-4ac}}{2a}$$

Consider the example, $a=1.0$, $b=2.0$, $c=-3.0$:

Using &ldquo;Python as a calculator&rdquo; we can find one of the solutions $x$ using

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FaPIcn1N9uZ.png?alt=media&token=19c4b5bd-8b9e-460e-add5-076b28385a5f)

(we will explain the use of `import math` and `math.sqrt` for calculating square roots below.)

This works, but the Python is complicated, making it easy to mistype something without realising it. It is also difficult to **understand** what this code is doing if you (or someone else) is reading it. And if we want to solve __another__ quadratic equation, then we need to retype the full equation with the new set of parameters (again, hoping we type everything correctly).

Using variables we can rewrite this calculation as:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FnQNXRcqxDJ.png?alt=media&token=16787e61-5f15-49ba-bcb6-edc85a1ac0cf)

This makes the calculation much more readable, and less prone to accidental errors when being typed. It is also clearer how we might adapt this to solve __another__ quadratic equation with different parameters $a$, $b$, and $c$—by editing the variables `a`, `b`, and `c`.

## Order of operations

Let us unpack this quadratic formula example a bit. We have already seen how simple mathematical operations can be expressed in Python. The full set of native mathematical operations in Python are

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FzZDZPWoEO8.png?alt=media&token=002ae382-008d-4300-95b9-bef341fb8e7a)

As we saw in the quadratic equation example, a single line of code can include more than one mathematical operation.

When an expression contains more than one mathematical operation, Python performs these according to a strict hierarchy necessary to follow a hierarchy, also known as the **order of operations**. Python follows the same order as standard mathematical notation: you may know this as [BODMAS](https://en.wikipedia.org/wiki/Order_of_operations).
- **B**rackets `()`
- **O**rder `**`
- **D**ivision `/` or `//`
- **M**ultiplication `*`
- **A**ddition `+`
- **S**ubtraction `-`

## The `math` module

Python provides access to more advanced mathematical functions using the `math` module. We will discuss modules in detail later. Here we will simply note that the `import math` command allows us to then use various functions  within the `math` module, using **dot syntax**:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FLbaHSWTQh_.png?alt=media&token=acb88555-4903-4d35-b66a-d0d013adb3dd)

