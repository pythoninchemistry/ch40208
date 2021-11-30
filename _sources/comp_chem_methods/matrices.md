# Matrices

## Matrices as linear transformations

We saw previously that the elements of a vector can be thought of as the coefficients in a linear combination of basis vectors, i.e. 

$$\begin{bmatrix}a\\b\end{bmatrix}=(a, b)=a\times\mathbf{i}+b\times\mathbf{j}$$

This means that a specific vector is only meaningful if the corresponding basis is defined. A suitable choice of basis vectors depends on the problem we are interested in solving, and there are many situations where it can be useful to change from one set of basis vectors to another: for example a molecular dynamics simulation might use atomic positions, velocities, and accelerations in Cartesian coordinates, corresponding to a Cartesian basis, and usually called the **lab** frame of reference. The dynamics of individual molecules, however, might be easier to describe within a **molecular** frame of reference, with basis vectors aligned with specific bonds or along rotational axes. In this case, modelling our system involves **transforming** between these two sets of basis vectors.

As an example consider the following figure:

:::{figure,myclass} rotation-example-fig
<img src="https://github.com/pythoninchemistry/ch40208/raw/master/CH40208/comp_chem_methods/figures/vectors_and_matrices/rotation_example.svg" width="650px" /> 

An example of a linear transformation: rotation by 90&deg; anticlockwise.
:::

This shows an initial basis with $\bvec{i}=\cvec{1}{0}$ and $\bvec{j}=\cvec{0}{1}$, and a vector $\bvec{r}$:
\begin{equation*}
\bvec{r}=\cvec{3}{4}=3\bvec{i}+4\bvec{j}. 
\end{equation*}
We now rotate our basis by 90&deg; anti-clockwise, which gives us a new vector $\bvec{r^\prime}$, which has elements $(3,4)$ in this new, rotated, basis;
\begin{equation*}
\bvec{r^\prime}=\cvec{3}{4}^\prime=3\bvec{i^\prime}+4\bvec{j^\prime},
\end{equation*}
where a prime symbol indicates we are in the new basis.

What is the vector $\bvec{r^\prime}$ in the **old** basis? We can see from the figure above that this should be $(-4,3)$, but can we calculate this?

We start by expressing the **new** basis vectors, $\bvec{i^\prime}$ and $\bvec{j^\prime}$, in terms of the **old** basis vectors, $\bvec{i}$ and $\bvec{j}$:
\begin{equation*}
\bvec{i^\prime} = (0\bvec{i}+1\bvec{j}) = \cvec{0}{1};
\end{equation*}
\begin{equation*}
\bvec{j^\prime} = (-1\bvec{i}+0\bvec{j}) = \cvec{-1}{0}.
\end{equation*}
We can now expand the vector $\bvec{r^\prime}$ in terms of $\bvec{i}$ and $\bvec{j}$:
\begin{eqnarray*}
\bvec{r^\prime}&=&(3\bvec{i^\prime}+4\bvec{j^\prime})\\
               &=&3(0\bvec{i}+1\bvec{j})+4(-1\bvec{i}+0\bvec{j})\\
               &=&-4\bvec{i}+3\bvec{j}.
\end{eqnarray*}
We can also write this as a single **matrix** equation, where we multiply each element of our original vector $\bvec{r}$ by the corresponding **column** of our matrix,
\begin{equation*}
\bvec{r^\prime} = \begin{bmatrix}0 & -1 \\ 1 & 0\end{bmatrix}\bvec{r}.
\end{equation*}
which looks like
\begin{eqnarray*}
\begin{bmatrix}0 & -1 \\ 1 & 0\end{bmatrix}\cvec{3}{4} & = & 3\cvec{0}{1}+4\cvec{-1}{0} \\
  & = & \cvec{0}{3} + \cvec{-4}{0} \\
  & = & \cvec{-4}{3}.
\end{eqnarray*}
If we denote our matrix as $\bvec{M}$, this can be written concisely as
\begin{equation*}
\bvec{r^\prime} = \bvec{M}\,\bvec{r}.
\end{equation*}

## Inverse matrix operations

We now have a matrix that describes a 90&deg; anti-clockwise rotation. What if we want to **invert** this rotation, and rotate by 90&deg; in a clockwise direction? If we follow the same procedure as above, we end up with a matrix $\bvec{N}=\begin{bmatrix}0 & 1\\ -1 & 0\end{bmatrix}$, where
\begin{equation*}
\bvec{r} = \bvec{N}\,\bvec{r^\prime}.
\end{equation*}
The matrix $\bvec{N}$ is called the **inverse** of the matrix $\bvec{M}$.

```{figure} https://github.com/pythoninchemistry/ch40208/raw/master/CH40208/comp_chem_methods/figures/vectors_and_matrices/rotation_example_inv.svg 
---
widhth: 650px
name: rotation-example-inv-fig
---
Rotating back by 90&deg; clockwise is the **inverse** of our previous 90&deg; anti-clockwise rotation, and is described by the **inverse** matrix operation.
```

## Matrix&ndash;matrix multiplication

What happens if we perform two matrix operations, one after the other? For example we perform **two** successive 90&deg; rotations&mdash;giving a 180&deg; rotation?

Mathematically this looks like
\begin{eqnarray*}
\bvec{r^{\prime\prime}}&=&\bvec{M}\,\bvec{r^\prime} \\
& = & \bvec{M}\left(\bvec{M}\,\bvec{r}\right) \\
& = & \bvec{M}\,\bvec{M}\,\bvec{r}.
\end{eqnarray*}
We first operate on $\bvec{r}$ with $M$, to get $\bvec{r^\prime}$, and then operate on this vector again with $\bvec{M}$. What is the result of this double operation, and can find a matrix that describes a general rotation by 180&deg;?

Written out, $\bvec{M}\,\bvec{M}$ looks like
\begin{equation*}
\bvec{M}\,\bvec{M}= \begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}.
\end{equation*}
We can determine the corresponding matrix for a 180&deg; rotation by considering what happens to the basis vectors $\bvec{i}$ and $\bvec{j}$ when we operate on them twice with $\bvec{M}$.
\begin{eqnarray*}
\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\bvec{i} = \begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\cvec{1}{0}
\end{eqnarray*}
As we saw above, the first operation (working from right to left) converts $\bvec{i}$ to $\bvec{i^\prime}=\cvec{0}{1}$. We now calculate the effect of the second operation
\begin{equation*}
\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\cvec{0}{1} = 0\cvec{0}{1} + 1\cvec{-1}{0} = \cvec{-1}{0}.
\end{equation*}
Doing the same for $\bvec{j^\prime}$ gives
\begin{equation*}
\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\cvec{-1}{0} = -1\cvec{0}{1} + 0\cvec{-1}{0} = \cvec{0}{-1}.
\end{equation*}
And we remember that the columns of a matrix describe the new basis functions, in this case $\bvec{i^{\prime\prime}}$ and $\bvec{j^{\prime\prime}}$. The matrix that describes a 180&deg; rotation (or two successive 90&deg; rotations) is therefore $\begin{bmatrix}-1 & 0\\ 0 & -1\end{bmatrix}$, i.e. both $x$ and $y$ are inverted.

:::{figure,myclass} rotation-example-twice-fig
<img src="https://github.com/pythoninchemistry/ch40208/raw/master/CH40208/comp_chem_methods/figures/vectors_and_matrices/rotation_example_twice.svg" width="650px" /> 

Rotating by 180&deg; corresponds to rotating by 90&deg; twice. We can calculate the corresponding matrix operation by considering what happens when we operate on our original basis *twice* with our 90&deg;-rotation matrix.
:::
