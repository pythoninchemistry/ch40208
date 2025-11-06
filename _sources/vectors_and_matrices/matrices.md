# Matrices

## Matrices as linear transformations

We saw previously that the elements of a vector can be thought of as the coefficients in a linear combination of basis vectors, i.e. 

$$
\begin{bmatrix}a\\b\end{bmatrix}=(a, b)=a\times\mathbf{i}+b\times\mathbf{j}
$$

This means that a specific vector is only meaningful if the corresponding basis is defined. A suitable choice of basis vectors depends on the problem we are interested in solving, and there are many situations where it can be useful to change from one set of basis vectors to another: for example a molecular dynamics simulation might use atomic positions, velocities, and accelerations in Cartesian coordinates, corresponding to a Cartesian basis, and usually called the **lab** frame of reference. The dynamics of individual molecules, however, might be easier to describe within a **molecular** frame of reference, with basis vectors aligned with specific bonds or along rotational axes. In this case, modelling our system involves **transforming** between these two sets of basis vectors.

As an example consider the following figure:

```{figure} ./figures/rotation_example.svg
---
width: 650px
name: rotation-example-fig
---
An example of a linear transformation: rotation by 90&deg; anticlockwise.
```

This shows an initial basis with $\mathbf{i}=\begin{bmatrix}1\\0\end{bmatrix}$ and $\mathbf{j}=\begin{bmatrix}0\\1\end{bmatrix}$, and a vector $\mathbf{r}$:

$$
\mathbf{r}=\begin{bmatrix}3\\4\end{bmatrix}=3\mathbf{i}+4\mathbf{j}. 
$$

We now rotate our basis by 90&deg; anti-clockwise, which gives us a new vector $\mathbf{r^\prime}$, which has elements $(3,4)$ in this new, rotated, basis;

$$
\mathbf{r^\prime}=\begin{bmatrix}3\\4\end{bmatrix}^\prime=3\mathbf{i^\prime}+4\mathbf{j^\prime},
$$

where a prime symbol indicates we are in the new basis.

What is the vector $\mathbf{r^\prime}$ in the **old** basis? We can see from the figure above that this should be $(-4,3)$, but can we calculate this?

We start by expressing the **new** basis vectors, $\mathbf{i^\prime}$ and $\mathbf{j^\prime}$, in terms of the **old** basis vectors, $\mathbf{i}$ and $\mathbf{j}$:

$$
\mathbf{i^\prime} = (0\mathbf{i}+1\mathbf{j}) = \begin{bmatrix}0\\1\end{bmatrix};
$$

$$
\mathbf{j^\prime} = (-1\mathbf{i}+0\mathbf{j}) = \begin{bmatrix}-1\\0\end{bmatrix}.
$$

We can now expand the vector $\mathbf{r^\prime}$ in terms of $\mathbf{i}$ and $\mathbf{j}$:

$$
\begin{aligned}
\mathbf{r^\prime}&=&(3\mathbf{i^\prime}+4\mathbf{j^\prime})\\
               &=&3(0\mathbf{i}+1\mathbf{j})+4(-1\mathbf{i}+0\mathbf{j})\\
               &=&-4\mathbf{i}+3\mathbf{j}.
\end{aligned}
$$

We can also write this as a single **matrix** equation, where we multiply each element of our original vector $\mathbf{r}$ by the corresponding **column** of our matrix,

$$
\mathbf{r^\prime} = \begin{bmatrix}0 & -1 \\ 1 & 0\end{bmatrix}\mathbf{r}.
$$

which looks like

$$
\begin{aligned}
\begin{bmatrix}0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix}3\\4\end{bmatrix}   & = & 3\begin{bmatrix}0\\1\end{bmatrix}&+&4\begin{bmatrix}-1\\0\end{bmatrix} \\
  & = & \begin{bmatrix}0\\3\end{bmatrix} &+& \begin{bmatrix}-4\\0\end{bmatrix} \\
  & = & \begin{bmatrix}-4\\3\end{bmatrix}&&.
\end{aligned}
$$

If we denote our matrix as $\mathbf{M}$, this can be written concisely as

$$
\mathbf{r^\prime} = \mathbf{M}\,\mathbf{r}.
$$

## Inverse matrix operations

We now have a matrix that describes a 90&deg; anti-clockwise rotation. What if we want to **invert** this rotation, and rotate by 90&deg; in a clockwise direction? If we follow the same procedure as above, we end up with a matrix $\mathbf{N}=\begin{bmatrix}0 & 1\\ -1 & 0\end{bmatrix}$, where

$$
\mathbf{r} = \mathbf{N}\,\mathbf{r^\prime}.
$$

The matrix $\mathbf{N}$ is called the **inverse** of the matrix $\mathbf{M}$.

```{figure} ./figures/rotation_example_inv.svg 
---
width: 650px
name: rotation-example-inv-fig
---
Rotating back by 90&deg; clockwise is the **inverse** of our previous 90&deg; anti-clockwise rotation, and is described by the **inverse** matrix operation.
```

## Matrix&ndash;matrix multiplication

What happens if we perform two matrix operations, one after the other? For example we perform **two** successive 90&deg; rotations&mdash;giving a 180&deg; rotation?

Mathematically this looks like

$$
\begin{aligned}
\mathbf{r^{\prime\prime}}&=&\mathbf{M}\,\mathbf{r^\prime} \\
& = & \mathbf{M}\left(\mathbf{M}\,\mathbf{r}\right) \\
& = & \mathbf{M}\,\mathbf{M}\,\mathbf{r}.
\end{aligned}
$$

We first operate on $\mathbf{r}$ with $M$, to get $\mathbf{r^\prime}$, and then operate on this vector again with $\mathbf{M}$. What is the result of this double operation, and can find a matrix that describes a general rotation by 180&deg;?

Written out, $\mathbf{M}\,\mathbf{M}$ looks like

$$
\mathbf{M}\,\mathbf{M}= \begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}.
$$

We can determine the corresponding matrix for a 180&deg; rotation by considering what happens to the basis vectors $\mathbf{i}$ and $\mathbf{j}$ when we operate on them twice with $\mathbf{M}$.

$$
\begin{aligned}
\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\mathbf{i} = \begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix}
\end{aligned}
$$

As we saw above, the first operation (working from right to left) converts $\mathbf{i}$ to $\mathbf{i^\prime}=\begin{bmatrix}0\\1\end{bmatrix}$. We now calculate the effect of the second operation

$$
\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}0\\1\end{bmatrix} = 0\begin{bmatrix}0\\1\end{bmatrix} + 1\begin{bmatrix}-1\\0\end{bmatrix} = \begin{bmatrix}-1\\0\end{bmatrix}.
$$

Doing the same for $\mathbf{j^\prime}$ gives

$$
\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}\begin{bmatrix}-1\\0\end{bmatrix} = -1\begin{bmatrix}0\\1\end{bmatrix} + 0\begin{bmatrix}-1\\0\end{bmatrix} = \begin{bmatrix}0\\-1\end{bmatrix}.
$$

And we remember that the columns of a matrix describe the new basis functions, in this case $\mathbf{i^{\prime\prime}}$ and $\mathbf{j^{\prime\prime}}$. The matrix that describes a 180&deg; rotation (or two successive 90&deg; rotations) is therefore $\begin{bmatrix}-1 & 0\\ 0 & -1\end{bmatrix}$, i.e. both $x$ and $y$ are inverted.

```{figure} ./figures/rotation_example_twice.svg
---
width: 650px
name: rotation-example-twice-fig
---
Rotating by 180&deg; corresponds to rotating by 90&deg; twice. We can calculate the corresponding matrix operation by considering what happens when we operate on our original basis *twice* with our 90&deg;-rotation matrix.
```
