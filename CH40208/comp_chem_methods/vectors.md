# Vectors

Many problems in chemistry and physics involve working with <em>vector</em> quantities. A common definition of a vector in a physics context is a quantity with both <em>magnitude</em> and <em>direction</em>; for example, the positions or velocities of atoms, or the forces acting on atoms within a molecule.

## Example 1: Atomic positions.

Defining atomic positions requires three pieces of information: the location of some reference point in space, called the <em>origin</em>, the distance of each atom from the origin, and the direction we move from the origin to reach the atom. Positions are therefore [<em>vector</em> quantities](position-vector-1-fig), since they define both <em>magnitude</em> and <em>distance</em> (relative to the origin).

```{figure} ./figures/vectors_and_matrices/position_vectors_1.svg
---
width: 400 px
name: position-vector-1-fig
---
Defining atomic positions requires knowing both distance and direction with respect to some reference <em>origin</em>.
```

A common choice for describing atomic positions is to use Cartesian coordinates, i.e. $(x, y)$ in two dimensions, or $(x, y, z)$ in three dimensions [^footnote1]; this will be familiar from the earlier exercises on calculating interatomic distances.

In two dimensions, any position can be described by giving both the [$x$ and $y$ coordinate](position-vector-1-fig).

```{figure} ./figures/vectors_and_matrices/position_vectors_2.svg
---
width: 400px 
name: position-vector-2-fig
---
Describing positions using Cartesian coordinates, i.e. $(x, y)$ coordinates in two dimensions, or $(x, y, z)$ in three dimensions.
```

Using the language of vectors, this choice of $x$ and $y$ coordinates defines a pair of <em>basis vectors</em>, which we will denote $\mathbf{i}$ and $\mathbf{j}$. [^footnote2]

```{figure} ./figures/vectors_and_matrices/position_vectors_3.svg
---
width: 400px 
name: position-vector-3-fig
---
In two dimensions we have two implicit basis vectors $\mathbf{i}$ and $\mathbf{j}$. Any position can be expressed as a <em>linear combination</em> of these basis vectors.
```

Any position vector $r = (x, y)$ can be expressed as a <em>linear combination</em> of these basis vectors, i.e. $r = x \times \mathbf{i} + y \times \mathbf{j}$. This means one way to think about the usual notation $(x, y)$ is that the two numbers describe the coefficients of $\mathbf{i}$ and $\mathbf{j}$ for a given linear combination.

```{figure} ./figures/vectors_and_matrices/position_vectors_4.svg
---
name: position-vector-4-fig
width: 400px
---
The $(x, y)$ coordinates given [above](position-vector-2-fig) are the coefficients used to define each position in the basis $(\mathbf{i}, \mathbf{j})$.
```

This might seem an overly complicated way of thinking about coordinates in Cartesian space, but it highlights that writing down a position vector such as $(3, 4)$ is only meaningful if the basis vectors are defined. If we had chosen a different set of basis vectors, the <em>same</em> positions would be described with <em>different</em> vectors.

```{figure} ./figures/vectors_and_matrices/position_vectors_alternate_basis.svg
---
name: position-vector-alternate-basis-fig
width: 400px
---
The same three positions described using a different basis.
```

[^footnote1]:A good choice of coordinate system depends on the problem at hand, and Cartesian coordinates may not always be easiest to work with. For example, problems with spherical symmetry, such as describing atomic orbitals, will often be simpler when expressed in spherical coordinates $(r, \phi, \theta)$.

[^footnote2]:Vectors are usually distinguished from scalar variables by using upright bold text, e.g. $\mathbf{r}$ (used here) or an accenting arrow, e.g. $\vec{r}$. The components of a vector can be given as a list, e.g. $(1,2)$, or as a column vector, e.g. $\begin{bmatrix}1\\2\end{bmatrix}$. These two representations correspond to the same vector $1\vec{i}+2\vec{j}$.

## Vector addition, subtraction, scaling, and &ldquo;multiplication&rdquo;

Vectors can be added together by adding the coefficients of each basis vector.

```{figure} ./figures/vectors_and_matrices/vector_addition.svg
---
name: vector-addition-fig
width: 400px
---
Vector addition.
```

For example, adding together the vectors $\mathbf{v}_1=(5,1)$ and $\mathbf{v}_2=(2,4)$ gives us a new vector $\mathbf{v}_3=(7,6)$,
which can be understood by writing $\mathbf{v}_1$ as $(5\mathbf{i}+1\mathbf{j})$ and $\mathbf{v}_2$ as $(2\mathbf{i}+4\mathbf{j})$. Adding $\mathbf{v1}$ and $\mathbf{v2}$ then gives $\left[(5\mathbf{i}+1\mathbf{j})+(2\mathbf{i}+4\mathbf{j})\right]$ and common terms can be collected together to give $\left[(5+2)\mathbf{i}+(1+4)\mathbf{j}\right]=(7\mathbf{i}+6\mathbf{j})$. 

Subtracting one vector from another follows the same rules, but with the coefficients of each basis vector subtracted; e.g. $\mathbf{v}_1-\mathbf{v}_2=(3,-3)$.

Scaling a vector involves multiplying by a <em>scalar</em> (hence the name). This changes the length of the vector, but not the direction, and involves multiplying each of the basis vector coefficients by the scalar value. i.e. $\mathbf{v}_\mathrm{1}=(2,3)$. $\mathbf{v}_1\times2=(4,6)$. 
Again, we can understand this by expanding out the original vector in terms of the basis vectors, $\mathbf{i}$ and $\mathbf{j}$: $(2\mathbf{i}+3\mathbf{j})\times2=(4\mathbf{i}+6\mathbf{j})$.

### The dot-product and the cross-product

We can also &ldquo;multiply&rdquo; two vectors together, although this is more complex. In fact there are <em>two</em> standard ways to deinfe &ldquo;multiplication&rdquo; of vectors.

The <em>dot product</em> is also known as the &ldquo;scalar product&rdquo;. This operation takes two vectors and returns a scalar quantity. The dot product of two vectors is denoted $\mathbf{a}\cdot\mathbf{b}$, and is defined as

$$ \mathbf{a}\cdot\mathbf{b} = \sum_ia_ib_i = a_1b_1 + a_2b_2 + \ldots + a_nb_n.$$

For example, if $\mathbf{a}=(2,1)$ and $\mathbf{b}=(3,2)$ then $\mathbf{a}\cdot\mathbf{b}$ is given by

$$\begin{eqnarray*}
\mathbf{a}\cdot\mathbf{b} & = & (x_\mathrm{a} \times x_\mathrm{b})+ (y_\mathrm{a}\times y_\mathrm{b})\\
& = & (2\times3 + 1\times2) \\
& = & 8
\end{eqnarray*}$$

An equivalent definition of the dot product is

$$\mathbf{a}\cdot\mathbf{b} = \left\lVert\mathbf{a}\right\rVert \left\lVert\mathbf{b}\right\rVert \cos\theta,$$

where $\left\lVert\mathbf{a}\right\rVert$ is the _length_ of vector $\mathbf{a}$, and $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$.

The <em>cross-product</em> is also known as the &ldquo;vector product&rdquo;. This operation takes two vectors and returns a vector quantity, with both magnitude and direction. The cross product between vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted $\mathbf{a}\times\mathbf{b}$ and is defined as a vector <em>perpendicular</em> to the plane containing $\mathbf{a}$ and $\mathbf{b}$ with a length given by the area of the <em>parallelogram</em> with $\mathbf{a}$ and $\mathbf{b}$ as sides.

```{figure,myclass} ./figures/vectors_and_matrices/cross_product.svg
---
name: cross-product-fig
width: 500px
---
The cross product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is proportional to the area $A$ of the parallelogram with sides $\mathbf{a}$ and $\mathbf{b}$.
```

This can be computed as

$$\mathbf{a}\times\mathbf{b} = \left\lVert\mathbf{a}\right\rVert \left\lVert\mathbf{b}\right\rVert \sin\theta\,\mathbf{n},$$

where $\mathbf{n}$ is the <em>unit vector</em> (a vector with length 1) perpendicular to the plane containing $\mathbf{a}$ and $\mathbf{b}$.


