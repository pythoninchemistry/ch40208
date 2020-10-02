# Using Python as a calculator

## Calculating 2+2

One of the simplest uses of Python is as a simple calculator. 

This also introduces us to the idea of working with numbers which is a key part of using Python for scientific applications.

Open a new Notebook and enter into a **code cell**

```
2+2
```

Running this cell should give you the following output:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fnia6lzqGgW.png?alt=media&token=de1f1f20-0d4a-4a86-96ed-48d6c8005f0c)

You can add space between the numbers to make things easier to read:
```
2 + 2
```

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fc2SgMm2FWo.png?alt=media&token=3434d75c-4c83-4f63-8a33-a8c97a059fc7)

Or wrap the expression in brackets:
```
(2 + 2)
```

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FrdjVqGVGI5.png?alt=media&token=cb4b41bd-84f0-4a5b-aa90-f558e1314381)

And still get the same result.

## Simple arithmetic

You are not limited to adding numbers. Try entering the following expressions into code cells and **executing** them (running the cells.):
- subtraction:
```
3 - 1
```
- multiplication:
```
4 * 2
```
- powers (e.g. 4<sup>2</sup>)
```
4 ** 2
```
- division
```
6 / 2
```

## Integers and Floats

Notice that the last example gives `3.0` and not `3` as the result. Python distinguishes between **integers** (also called **ints**) and **floating point numbers** (also called **floats**):
- Integers: A number **without** a decimal point: e.g. 1, 2, 100, 10<sup>10</sup>.
- Floats: A number **with** a decimal point. e.g. 3.14159, 12.0107, 8.3144 (you might recognise these).

Arithmetic also works with **floats**:
```
2.0 + 2.0
```
```
4.0 * 2.0
```
```
4.0 ** 2.0
```
```
6.0 / 2.0
```

And with mixtures of **integers** and **floats**
```
2 + 2.0
```
```
4 * 2.0
```
```
4.0 ** 2
```
```
6 / 2.0
```
Notice how these last examples always output a **float**.

**floats** can also be written without any numbers after the decimal point, e.g.
```
42.
```
is the same as `42.0`.

You can do integer division (also called **floor division** ) using `//`:
```
6 // 2
```
Integer division rounds down:
```
7 // 2
```

You can calculate the **remainder** of integer division using the `%` symbol (called the **modulo** operator).
```
7 % 2
```
```
8 % 2
```

Brackets can be used to specify the order of operations in more complicated expressions, according to the usual mathematical rules:
```
(2 + 3) * 4
```
```
2 + (3 * 4)
```

We will return to mathematical expressions in Python in more detail later in the course.

