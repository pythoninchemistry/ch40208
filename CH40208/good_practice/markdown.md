# Markdown

The Jupyter Notebook framework is designed to enable text and code to live together. 
This was introduced [when you were first shown the Notebook interface](https://pythoninchemistry.org/ch40208/notebooks_introduction/the_notebook_interface.html), but here we want to talk a bit more about why and how we do this. 

We have made a lot of use of the Jupyter Notebook *Cells*, where we write our Python code. 
However, in the dropdown menu (identified in the figure below), we can change the type of our cell. 

![](https://github.com/pythoninchemistry/ch40208/raw/master/CH40208/good_practice/code_cell.png)

If we change this to *Markdown*, we can write plain text in our cell, and when it is *Run* the text is rendered clearly. 

Markdown is a simple [markup language](https://en.wikipedia.org/wiki/Markup_language) that allows us to write text to accompany our code. 
For example, if we want a heading we can use `#`, and the number of hash-symbols will control the heading size:

```
# Heading 1
## Heading 2
### Heading 3
```

Will render as 

# Heading 1
## Heading 2
### Heading 3

We can also add figures to our text, for example, this page is written in Markdown and to add the figure above, the following was written: 

```
![The cell type dropdown identified on a Notebook with the current selection as Code](https://github.com/pythoninchemistry/ch40208/raw/master/CH40208/good_practice/code_cell.png)
```

Where between the normal brackets is an image hosted online and the square brackets is a textual description of the figure. 

The final capability of Markdown we will talk about is the ability to render mathematical notation, this comes in the form of [LaTeX](https://en.wikipedia.org/wiki/LaTeX) support. 
LaTeX is a common way to write mathematical equations and a lot of documentation about how you use it. 
Here, we will just so that to activate a LaTeX math environment in our Notebook we can write the following in a Markdown cell. 

```
$$ e = mc^2
```

Which will be rendered as 

$$ e = mc^2 $$

Note, to have inline equations we can write `$y = mx + c$` which would appear as $y = mx+c$. 

Markdown as a lot of functionality that we will not discuss in detail. 
Good help for Markdown can be found online, including in the [Markdown Guide cheatsheet](https://www.markdownguide.org/basic-syntax/), we recommend using Google if you need help (that is what we do!).