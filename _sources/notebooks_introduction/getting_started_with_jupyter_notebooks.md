# Getting started with Jupyter Notebooks

## First Time Logging On to the JupyterHub Server

When you first log on to the [JupyterHub server](./how_to_access_the_jupyterhub_server.md) you should see a screen like this:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FyM-hR6PUUt.png?alt=media&token=45a46649-ac81-45d3-a8d2-a32c5078efd0)

This is the **Notebook Dashboard**, which allows you to access and manage your Jupyter Notebooks. The Dashboard allows you to create, open, rename, move, and delete Notebooks.

If you have just logged onto the JupyterHub server for the first time, You should have two items already listed in your Dashboard:
- A folder named `courses`.
- A Notebook named `Welcome.ipynb`.
  
The `.ipynb` file extension indicates that `Welcome.ipynb` is a Jupyter notebook.

### The Welcome Notebook

Clicking on `Welcome.ipynb` should open a new tab with the **Welcome Notebook** running inside it.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FbWPPWc4YEE.png?alt=media&token=2a489d08-7c67-4a90-ab4c-32c68fc6140d)

There is not much to see or do in this Notebook, but if you can open it up then you know that you have connected properly to the Jupyterhub Server and are able to run Notebooks.

The **Welcome Notebook** contains links to a set of other Notebooks; one for each course that will be using the Chemistry JupyterHub server for running Python. You will see a dedicated **CH40208 Notebook**:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F-bmvmUcXJb.png?alt=media&token=a294ab34-59c9-4287-b95d-6266697e39f3)
 
You can ignore this **CH40208 notebook** for the moment. Later in the course we will use the code in this notebook to copy any additional resources, such as prewritten notebooks or specialised Python modules, into your workspace.

If you close the tab that contains the `Welcome.ipynb` notebook you might notice something unexpected:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fb01JaIgYTG.png?alt=media&token=8c1695f1-cff0-44e7-afb6-17f4709080df)

The notebook icon next to `Welcome.ipynb` is now green, and on the right side you can see `Running`. We will explain what it means to have a Notebook "running" later. For the moment you can stop this Notebook running by selecting the checkbox to the left of the Notebook icon, and clicking `Shutdown` in the menubar above the list of files and folders.

<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FgIVJYktBPZ.png?alt=media&token=12065564-3232-4074-8265-bde939bbb892" width="25%" />
</p>

## Creating a new Jupyter Notebook

To create a new Notebook, click on `New` on the right-hand side of the screen, and then select `Python 3` from the drop-down menu:

<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F6JH_2wbf0f.png?alt=media&token=ea633874-fe66-46eb-99e0-326f8e625d2e" width="25%" />
</p>

This will open a brand new Notebook called `Untitled.ipynb`:

![A freshly created Notebook](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FUEJKQ9Cqrt.png?alt=media&token=f92a1060-6de9-4f01-b8f5-cbfc8b46d992)

## Renaming a Notebook

Naming your notebook`Untitled.ipynb`, or worse `Untitled37.ipynb`, is not very informative, and can be a problem when you come back to a project and need to find __just the right__ piece of data analysis. It is a good idea to give your Notebook a more meaningful name as soon as you create it.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FQI3sgceJlB.png?alt=media&token=4c54926e-66d9-44f4-b605-2e81afbbcce5)
<p align="center">Don't be this person.</p>

To rename your Notebook, you can either click on `File` -> `Rename…`:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FviJTCKJ7fP.png?alt=media&token=8dd1d082-5736-4e2d-94a9-c3851576040b)

Or click directly on the Notebook name (currently &ldquo;Untitled&rdquo;) at the top of the screen. Either way opens a `Rename Notebook` popup:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FctyiU8K7LR.png?alt=media&token=dd71722b-7b15-4fd4-b038-8a3e4f947acf)

To rename your Notebook, type in a new name and click `Rename`. (Go on, try it).

## Duplicating a Notebook

To duplicate your notebook, you can **make a copy** by selecting `File` -> `Make a Copy…`

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F7V1GxjbCtA.png?alt=media&token=9266e276-0f30-464b-950d-13ea3ccb92ff)

This opens another browser tab with your copied Notebook running in it. Your copy will have the same name as the original Notebook, but with `-Copy1` appended to the title (or `-Copy2` etc. if you have already created one copy).

Making a copy if useful if you want to make changes to a Notebook but you want to still be able to refer back to the original Notebook, or you might want a second Notebook that is similar to a Notebook you have already written, and you don't want to start from scratch; for example, if you are analysing data from a series of experiments and have created a notebook to run the analysis on one experiment, you might duplicate (copy) and then make minor changes to analyse the other experiments.

Just as it is bad practice to leave notebooks called `Untitled.ipynb` sitting around, you probably want to rename your duplicated notebook at the time of creation, instead of later wondering what the difference is between `Analysis.ipynb` and `Analysis-Copy3.ipynb`.

