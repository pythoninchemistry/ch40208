# Getting started with strings

We will also be working with pieces of text, which are represented in Python as **strings**.

A **string** must be enclosed in a matching pair of **single quotes** `'text goes here'` or **double quotes** `"text goes here"`.

Entering a string into a **code cell** and running the cell will just output the string:
```
'I am a string with single quotes'
```
```
"I am a string with double quotes"
```

Trying to pair single and double quotes will give an error or an unexpected output:
```
'I am a string with mismatched quotes"
```

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FnHqYMOChKp.png?alt=media&token=dc9aff05-113d-413d-9232-f24382f48989)

This gives a `SyntaxError`, which is one of the many error types invalid Python code can produce. A syntax error is one of the most basic error types and means that the Python interpreter is not able to understand the code.

We will dive into error messages and types of errors in Python in more detail later in the course.

You can include single quotes in a string that is enclosed in double quotes:
```
"Well isn't that clever?"
```
and double quotes in a string that is enclosed in single quotes:
```
'The cat asked, “Where do you want to go?”'
```
or you can indicate that quotes should be treated as text and not as string delimiters by preceding them with a backslash `\` (called **escaping** the quote):
```
'Well isn\'t that clever'
```

## Exercises:
Strings can be manipulated using *some* mathematical operations (but not others).  
Investigate what happens when you try:

- Adding two strings, using `+`.

- Subtracting one string from another, using `-`.

- Adding a string to an integer or a float, using `+`

- Mutiplying two strings together, using `*`.

- Multiplying a string by a float, using `*`.

- Multiplying a string by an integer, using `*`.

Can you reason why you get the results (and errors) that you do?

