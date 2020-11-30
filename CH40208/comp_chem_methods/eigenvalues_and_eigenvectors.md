# Eigenvalues and eigenvectors
We have seen that a matrix $\bvec{M}$ operating on a vector $\bvec{v}$ produces a new vector $\bvec{v^\prime}$:
\begin{equation*}
\bvec{v}^\prime = \bvec{M}\cdot\bvec{v}.
\end{equation*}
In general the matrix $\bvec{M}$ can change both the magnitude and direction of the vectors $\bvec{v}\to\bvec{v^\prime}$.

Consider the matrix $\bvec{M}=\tmatrix{2}{1}{1}{2}$. This gives the linear transformation shown below. 

:::{figure,myclass} matrix-transformation-fig
<img src="figures/vectors_and_matrices/matrix_transformation.svg" width="650px" />

The effect of the matrix $\bvec{M}=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ is to transform the basis vectors $\bvec{i}=\cvec{1}{0}$ and $\bvec{j}=\cvec{0}{1}$ (left) to $\bvec{i^\prime}=\cvec{2}{1}$ and $\bvec{j^\prime}=\cvec{1}{2}$ (right); i.e. the new unit vectors are the columns of $\bvec{M}$.
:::

We can also visualise this transformation by considering the effect on a set of vectors with length $1$ and different directions. Now we see that the effect of the matrix transformation is to transform a unit circle into an ellipse.

:::{figure,myclass} matrix-transformation-unit-circle-fig
<img src="figures/vectors_and_matrices/matrix_transformation_unit_circle.svg" width="650px" />

The effect of the matrix $\bvec{M}$ is to transform the unit circle (left) into an ellipse (right).
:::

The major and minor axes of this ellipse (given by the <em>longest</em> and <em>shortest</em> transformed vectors) lie along $\cvec{1}{1}$ and $\cvec{-1}{1}$, respectively. 

If we compare these transformed vectors to the corresponding <em>original</em> vectors we see that the effect of $\bvec{M}$ operating on these two vectors is only to <em>scale</em> them. Their directions have not changed. Mathematically, this can be expressed as
\begin{eqnarray*}
\bvec{v^\prime}&=&\bvec{M}\cdot\bvec{v} \\
s\bvec{v}&=&\bvec{M}\cdot\bvec{v}.
\end{eqnarray*}
i.e. operating on $\bvec{v}$ by $\bvec{M}$ gives the <em>same vector</em> $\bvec{v}$ back, times a <em>scalar</em>, $s$. This only happens for these two &ldquo;special&rdquo; vectors, which we call the <em>eigenvectors</em> of the matrix $\bvec{M}$. The scalar values $s$ are the <em>eigenvalues</em> of the matrix $\bvec{M}$.

:::{figure,myclass} ellipse-major-minor-axes-transformation-fig
<img src="figures/vectors_and_matrices/ellipse_major_minor_axes_transformation.svg" width="650px" />

Left: The two vectors corresponding to the major and minor axes of the ellipse in the [previous figure](matrix-transformation-unit-circle-fig). Right: The same two vectors <em>before</em> the transformation. Both of these vectors have the same direction before and after the transformation by $\bvec{M}$ and are <em>eigenvectors</em> of $\bvec{M}$.
:::

We can calcuate the eigenvalues and eigenvectors of a matrix using [`np.linalg.eig()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html):
```python
>>> print(np.linalg.eig(M))
(array([3., 1.]), array([[ 0.70710678, -0.70710678],
       [ 0.70710678,  0.70710678]]))
```
This returns two arrays. The first array contains the eigenvalues of $\bvec{M}$, and the second array contains the eigenvectors of $\bvec{M}$.
```python
>>> print(np.linalg.eig(M)[0])
[3., 1]
>>> print(np.linalg.eig(M)[1])
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
```
Note that the eigenvectors are returned as a matrix. Each of the <em>columns</em> of this matrix correspond to one of the eigenvectors. We can see that for the matrix $\bvec{M}=\tmatrix{2}{1}{1}{2}$ we get one eigenvector $\cvec{0.70710678}{0.70710678}$ with eigenvalue $3$, and a second eigenvector $\cvec{-0.70710678}{\phantom{-}0.70710678}$ with eigenvalue $1$.

Calculating eigenvalues and eigenvectors has applications in a number of areas of chemistry. For example:
- Describing the rotational motions of molecules: finding principal axes of rotation and principal moments of inertia (eigenvectors and eigenvalues of the inertia matrix).
- Describing the vibrational motions of molecules: finding normal modes (eigenvectors and eigenvalues of the dynamical matrix).
- Solving the time-independent Schr&ouml;dinger equation $\bvec{H}\Psi=E\Psi$, which is an eigenvalue equation: finding molecular orbitals and their corresponding energies (eigenvectors and eigenvalues of the Hamiltonian matrix).

```{admonition} Key ideas
:class: tip
- A two-dimensional matrix transforms a unit circle into an ellipse.
- A vector that does not change direction under the operation $\bvec{M}$ is an <em>eigenvector</em> of $\bvec{M}$. The scaling factor of this vector is the corresponding <em>eigenvalue</em>.
```
