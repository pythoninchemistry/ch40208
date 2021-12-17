# Eigenvalues and eigenvectors
We have seen that a matrix $\mathbf{M}$ operating on a vector $\mathbf{v}$ produces a new vector $\mathbf{v^\prime}$:

$$
\mathbf{v}^\prime = \mathbf{M}\cdot\mathbf{v}.
$$

In general the matrix $\mathbf{M}$ can change both the magnitude and direction of the vectors $\mathbf{v}\to\mathbf{v^\prime}$.

Consider the matrix $\mathbf{M}=\begin{bmatrix}2 & 1 \\ 1 & 2\end{bmatrix}$. This gives the linear transformation shown below. 


```{figure} ./figures/vectors_and_matrices/matrix_transformation.svg
---
width: 650px
name: matrix-transformation-fig
---

The effect of the matrix $\mathbf{M}=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ is to transform the basis vectors $\mathbf{i}=\begin{bmatrix}1 \\ 0\end{bmatrix}$ and $\mathbf{j}=\begin{bmatrix}0 \\ 1\end{bmatrix}$ (left) to $\mathbf{i^\prime}=\begin{bmatrix}2 \\ 1\end{bmatrix}$ and $\mathbf{j^\prime}=\begin{bmatrix}1 \\ 2\end{bmatrix}$ (right); i.e. the new unit vectors are the columns of $\mathbf{M}$.
```

We can also visualise this transformation by considering the effect on a set of vectors with length $1$ and different directions. Now we see that the effect of the matrix transformation is to transform a unit circle into an ellipse.

```{figure} ./figures/vectors_and_matrices/matrix_transformation_unit_circle.svg
---
width: 650px
name: matrix-transformation-unit-circle-fig
---

The effect of the matrix $\mathbf{M}$ is to transform the unit circle (left) into an ellipse (right).
```

The major and minor axes of this ellipse (given by the <em>longest</em> and <em>shortest</em> transformed vectors) lie along $\begin{bmatrix}1 \\ 1\end{bmatrix}$ and $\begin{bmatrix}-1 \\ 1\end{bmatrix}$, respectively. 

If we compare these transformed vectors to the corresponding <em>original</em> vectors we see that the effect of $\mathbf{M}$ operating on these two vectors is only to <em>scale</em> them. Their directions have not changed. Mathematically, this can be expressed as

$$
\begin{aligned}
\mathbf{v^\prime}&=&\mathbf{M}\cdot\mathbf{v} \\
s\mathbf{v}&=&\mathbf{M}\cdot\mathbf{v}.
\end{aligned}
$$

i.e. operating on $\mathbf{v}$ by $\mathbf{M}$ gives the <em>same vector</em> $\mathbf{v}$ back, times a <em>scalar</em>, $s$. This only happens for these two &ldquo;special&rdquo; vectors, which we call the <em>eigenvectors</em> of the matrix $\mathbf{M}$. The scalar values $s$ are the <em>eigenvalues</em> of the matrix $\mathbf{M}$.

```{figure} ./figures/vectors_and_matrices/ellipse_major_minor_axes_transformation.svg
---
width: 650px
name: ellipse-major-minor-axes-transformation-fig
---

Left: The two vectors corresponding to the major and minor axes of the ellipse in the [previous figure](matrix-transformation-unit-circle-fig). Right: The same two vectors <em>before</em> the transformation. Both of these vectors have the same direction before and after the transformation by $\mathbf{M}$ and are <em>eigenvectors</em> of $\mathbf{M}$.
```

We can calcuate the eigenvalues and eigenvectors of a matrix using [`np.linalg.eig()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html):
```python
>>> print(np.linalg.eig(M))
(array([3., 1.]), array([[ 0.70710678, -0.70710678],
       [ 0.70710678,  0.70710678]]))
```
This returns two arrays. The first array contains the eigenvalues of $\mathbf{M}$, and the second array contains the eigenvectors of $\mathbf{M}$.
```python
>>> print(np.linalg.eig(M)[0])
[3., 1]
>>> print(np.linalg.eig(M)[1])
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
```
Note that the eigenvectors are returned as a matrix. Each of the <em>columns</em> of this matrix correspond to one of the eigenvectors. We can see that for the matrix $\mathbf{M}=\begin{bmatrix}2 & 1 \\ 1 & 2\end{bmatrix}$ we get one eigenvector $\begin{bmatrix}0.70710678 \\ 0.70710678 \end{bmatrix}$ with eigenvalue $3$, and a second eigenvector $\begin{bmatrix} -0.70710678 \\ \phantom{-}0.70710678\end{bmatrix}$ with eigenvalue $1$.

Calculating eigenvalues and eigenvectors has applications in a number of areas of chemistry. For example:
- Describing the rotational motions of molecules: finding principal axes of rotation and principal moments of inertia (eigenvectors and eigenvalues of the inertia matrix).
- Describing the vibrational motions of molecules: finding normal modes (eigenvectors and eigenvalues of the dynamical matrix).
- Solving the time-independent Schr&ouml;dinger equation $\mathbf{H}\Psi=E\Psi$, which is an eigenvalue equation: finding molecular orbitals and their corresponding energies (eigenvectors and eigenvalues of the Hamiltonian matrix).

```{admonition} Key ideas
:class: tip
- A two-dimensional matrix transforms a unit circle into an ellipse.
- A vector that does not change direction under the operation $\mathbf{M}$ is an <em>eigenvector</em> of $\mathbf{M}$. The scaling factor of this vector is the corresponding <em>eigenvalue</em>.
```
