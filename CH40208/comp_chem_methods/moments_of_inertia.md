# Principal rotation axes and principal moments of inertia

The rotational energy levels of a molecule depend upon the molecule's moments of inertia, making these important molecular quantities for interpreting rotational spectra, or for calculating the rotational partition function:

$$
q_\mathrm{rot} = \frac{\pi^{\frac{1}{2}}}{\sigma}\left(\frac{k_\mathrm{B}T}{hcA}\right)^\frac{1}{2}\left(\frac{k_\mathrm{B}T}{hcB}\right)^\frac{1}{2}\left(\frac{k_\mathrm{B}T}{hcC}\right)^\frac{1}{2},
$$

where $A$, $B$, and $C$ and the <em>principal moments of inertia</em> of a non-linear molecule.

Moments of inertia, described by $\mathbf{I}$, describe how a rigid body responds to angular acceleration, and are analogous to inertial mass for linear acceleration:

$$
\begin{aligned}
\mathbf{F} = m\mathbf{a} && \mathbf{\tau} = \mathbf{I}\mathbf{\alpha} \\
\mathbf{p} = m\mathbf{v} && \mathbf{L}    = \mathbf{I}\mathbf{\omega}
\end{aligned}
$$

Where $\mathbf{\alpha}$ is angular acceleration and $\mathbf{\tau}$ is torque, and $\mathbf{\omega}$ is angular velocity and $\mathbf{L}$ is angular momentum.

If we focus on angular momentum, then for a one-dimensional problem, where rotation occurs around a single axis (e.g. for a diatomic molecule), $\mathbf{\omega}$ and $\mathbf{L}$ are scalars and $\mathbf{I}$ is also a scalar:

$$
L = I\omega
$$ 

For a rigid diatomic molecule the moment of inertia, $I$, is given by

$$
I = \sum_i m_i r_i^2
$$

where $r_i$ is the distance of each atom from the centre of mass. This is often written in terms of the <em>reduced mass</em> of the molecule, $\mu$:

$$
I = \mu r^2
$$

where $r$ is the molecular bond length.

In three dimensions, however, $\mathbf{\omega}$, and $\mathbf{L}$ are <em>vectors</em>, and are not required to have the same orientation. The quantity $\mathbf{I}$, which translates one vector into another vector, is therefore a <em>matrix</em>, called the <em>inertia matrix</em>:

$$
\begin{bmatrix}L_x\\L_y\\L_z\end{bmatrix} = 
\begin{bmatrix} 
\phantom{-}I_{xx} & -I_{xy} & -I_{xz} \\
-I_{yx} & \phantom{-}I_{yy} & -I_{yz} \\
-I_{zx} & -I_{zy} & \phantom{-}I_{zz} 
\end{bmatrix}
\cdot
\begin{bmatrix}\omega_x\\\omega_y\\\omega_z\end{bmatrix}.
$$

where the <em>diagonal</em> elements (called &ldquo;moments of inertia&rdquo;) are similar to the one-dimensional definition, e.g.

$$
\begin{aligned}
I_{xx} = \sum_i m_i(y_i^2+z_i^2), \\
I_{yy} = \sum_i m_i(x_i^2+z_i^2), \\
I_{zz} = \sum_i m_i(x_i^2+y_i^2);
\end{aligned}
$$

but the <em>off-diagonal</em> elements (called &ldquo;products of inertia&rdquo;) must also be included:

$$
\begin{aligned}
I_{xy} = \sum_i m_ix_iy_i, \\
I_{xz} = \sum_i m_ix_iz_i, \\
I_{yz} = \sum_i m_iy_iz_i.
\end{aligned}
$$

In the case of a rotation molecule, the index $i$ runs over the atoms in the molecule.

Having non-zero off-diagonal elements in the intertia matrix makes working with angular motion in 3D more complicated than in 1D. It is often useful therefore to seek a simpler form for $\mathbf{I}$ that gives a more intuitive description of molecular rotational properties.

Each of the elements of $\mathbf{I}$ contains terms like
$x_i^2$
or $xy$, where $x$, $y$, and $z$ are distances of atoms along each direction from the centre of mass. The values of each element of $\mathbf{I}$ therefore depend on the relative orientation of the $\left\{x,y,z\right\}$ coordinate system and the molecule. Choosing a differently oriented coordinate system changes the $x$, $y$, and $z$ coordinates of each atom, and changes the values of the elements of $\mathbf{I}$. We might therefore ask: is there a choice of molecular orientation / coordinate orientation where the off-diagonal elements of $\mathbf{I}$ are all zero?

If this were the case, our angular momentum equation would now be:

$$
\begin{bmatrix}L_x\\L_y\\L_z\end{bmatrix} = 
\begin{bmatrix} 
I_{xx} & 0 & 0 \\
0 & I_{yy} & 0 \\
0 & 0 & I_{zz} 
\end{bmatrix}
\cdot
\begin{bmatrix}\omega_x\\\omega_y\\\omega_z\end{bmatrix}.
$$

and each component of $\mathbf{l}$ would be directly proportional to the corresponding component of $\mathbf{w}$. The "products of inertia" now do not appear, and we can describe the rotational properties of the molecule by specifying the three moments of inertia.

It turns out that such a coordinate system can be found, and it corresponds to choosing the <em>eigenvectors</em> of $\mathbf{I}$ as our basis vectors. Let us suppose that we have found the eigenvalues, $\lambda_i$, and eigenvectors, $\mathbf{v}_i$, of $\mathbf{I}$. This gives us three eigenvalue equations:

$$
\begin{aligned}
\lambda_1 \mathbf{v}_1 & = & \mathbf{I}\cdot\mathbf{v}_1 \\
\lambda_2 \mathbf{v}_2 & = & \mathbf{I}\cdot\mathbf{v}_2 \\
\lambda_3 \mathbf{v}_3 & = & \mathbf{I}\cdot\mathbf{v}_3.
\end{aligned}
$$

Let us now express our angular velocity vector $\mathbf{\omega}$ using these eigenvectors as a basis:

$$
\mathbf{\omega} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3.
$$

And then the effect of the matrix $\mathbf{I}$ operating on $\mathbf{\omega}$:

$$
\begin{aligned}
\mathbf{I}\cdot\mathbf{\omega} & = & c_1\mathbf{I}\cdot\mathbf{v}_1 + c_2\mathbf{I}\cdot\mathbf{v}_2 + c_3\mathbf{I}\cdot\mathbf{v}_3 \\
& = & c_1\lambda_1\mathbf{v}_1 + c_2\lambda_1\mathbf{v}_2 + c_3\lambda_1\mathbf{v}_3.
\end{aligned}
$$

which can be rewritten in matrix form as

$$
\begin{aligned}
\mathbf{I}\cdot\mathbf{\omega} & = & 
\begin{bmatrix} 
\lambda_1 & 0 & 0 \\
0 & \lambda_2 & 0 \\
0 & 0 & \lambda_3
\end{bmatrix}
\cdot
\begin{bmatrix}c_1\\c_2\\c_3\end{bmatrix} \\
& = & \begin{bmatrix} 
\lambda_1 & 0 & 0 \\
0 & \lambda_2 & 0 \\
0 & 0 & \lambda_3
\end{bmatrix}
\cdot
\mathbf{\omega}
\end{aligned}
$$

This gives the simplified form that we wanted, <em>if</em> we use the eigenvectors of $\mathbf{I}$ as our basis vectors, i.e. as our coordinate system vectors. The eigenvectors of the inertia matrix are called the <em>principal rotation axes</em> of our molecule, and the corresponding eigenvalues are the <em>principal moments of inertia</em>.

For a molecule in an arbitrary orientation, we can therefore calculate the principal moments of inertia by finding the eigenvalues of the inertia matrix. The corresponding eigenvectors give us the principal rotation axes, which are often used to define a &ldquo;natural&rdquo; coordinate system for the molecule.

## Rotating molecules onto their principal rotation axes
If the principal rotation axes of a molecule define a natural coordinate system for that molecule, are we able to rotate an arbitrarily oriented molecule onto this coordinate system? The answer is yes, and it builds on our understanding of <em>rotation matrices</em> and <em>eigenvectors</em>.

For a given molecular rotation, the basis vectors $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ point along $x$, $y$, and $z$ respectively. But we would like to rotate our molecule so that $x$, $y$, and $z$ point along the principal rotation axes of the molecule. This is equivalent to <em>transforming</em> our coordinate system so that $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ are aligned with the eigenvectors of the inertia matrix $\mathbf{I}$ (for the original coordinate system). Remember that a matrix transformation maps the original basis vectors onto the columns of the matrix. To map $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ onto $\mathbf{v}_1$, $\mathbf{v}_2$, and $\mathbf{v}_3$ we would operate on the vector coordinates of the atoms in the molecule with a matrix composed of $\mathbf{k}$ onto $\mathbf{v}_1$, $\mathbf{v}_2$, and $\mathbf{v}_3$ as columns. This would rotate our basis vectors to align with the molecular principal axes. However, we want to do the <em>inverse</em> of this operation, and rotate the principal axes of the molecule to align with our coordinate system. Our rotation matrix is therefore the <em>inverse</em> matrix

$$
\begin{bmatrix}\phantom{0}\\\mathbf{v}_1&\mathbf{v}_2&\mathbf{v}_3\\\phantom{0}\end{bmatrix}^{-1}.
$$


## Exercise

The following exercise is to calculate principal moments of inertia and principal rotation axes of a series of molecules, and then to rotate these molecules so that the principal axes are aligned with $\left\{x, y, z\right\}$.

The coordinates of each molecule can be downloaded using the links below, along with a ``visualisation2.py`` module that contains some code for visualising your molecules and their orientations.

### Files to download

- <a href="../data/rigid_rotor.dat" download>`rigid_rotor.dat`</a>
- <a href="../data/water.dat" download>`water.dat`</a>
- <a href="../data/ethane.dat" download>`ethane.dat`</a>
- <a href="../data/ammonia.dat" download>`ammonia.dat`</a>
- <a href="../data/chloromethane.dat" download>`chloromethane.dat`</a>
- <a href="../data/methane.dat" download>`methane.dat`</a>
- <a href="../data/visualisation2.py" download>`visualisation2.py`</a>

### Details

In terms of planning your code, you want to be able to perform the following sequence of steps:
1. Each file contains data in the format $\left\{x, y, z, m\right\}$ for each atom, where $m$ is the atomic mass of that atom. You will first want to read this in, and extract the atomic coordinates and masses.
2. Construct the inertia matrix $\mathbf{I}$.
3. Calculate the eigenvalues and eigenvectors of $\mathbf{I}$.
4. Operate on your atomic coordinates to generate new coordinates, with the molecular principal axes aligned with $\left\{x, y, z\right\}$.
5. Use the ``visualisation.show()`` function to look at your rotated molecules. Do these look how you would expect from what you know about molecular symmetry?
