## The Mechanics of Molecular Dynamics

To understand how molecular dynamics works, consider a simple analogy: a ball rolling across hills and valleys.
At any moment, the ball has a defined position $r$, velocity $v$, and mass $m$. The shape of the terrain—our potential energy surface $U(r)$—determines how the ball will move. From this potential energy surface, we can calculate two crucial quantities: first, the force acting on the ball ($F = -\frac{\mathrm{d}U}{\mathrm{d}r}$), and second, using Newton's second law ($F = ma$), the ball's acceleration $a$.

The ball's motion is described by two fundamental differential equations:
\begin{equation}
\frac{\mathrm{d}r}{\mathrm{d}t} = v
\end{equation}
\begin{equation}
\frac{\mathrm{d}v}{\mathrm{d}t} = a
\end{equation}

By integrating these equations of motion, we can derive expressions for the changes in position and velocity over a time interval $\delta t$:
\begin{equation}
\frac{dv}{dt} = a \rightarrow v(t + \delta t) = v(t) + a(t)\delta t
\end{equation}
\begin{equation}
\frac{dr}{dt} = v \rightarrow r(t + \delta t) = r(t) + v(t)\delta t + \frac{1}{2}a(t)\delta t^2
\end{equation}
These equations are exact as $\delta t$ approaches zero. For practical calculations, however, we need to work with finite time intervals. We introduce a "timestep" $\Delta t$ and use these equations to predict how our system evolves:

From the current position $r(t)$, we calculate the force $F(r) = -\frac{\mathrm{d}U(r)}{\mathrm{d}r}$.

From this force and the ball's mass, we determine the acceleration $a(t) = F(r)/m$.

Using $r(t)$, $v(t)$, and $a(t)$, we can approximately calculate $r(t+\Delta t)$ and $v(t+\Delta t)$.

By repeating this process—using each new position and velocity to calculate the next—we can trace the ball's entire trajectory through time.
