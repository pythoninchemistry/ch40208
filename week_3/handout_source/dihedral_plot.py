import numpy as np
import matplotlib.pyplot as plt

A1 = 55.22880
A2 = 3.34720
A3 = -58.57600


def energy(phi):
    return 0.5 * (A1 * (1 + np.cos(phi)) + A2 * (1 + np.cos(2 * phi)) + A3 * (
        1 + np.cos(3 * phi)))


p = np.linspace(-np.pi, np.pi, 100)
plt.plot(p, energy(p))
plt.ylabel(r'Energy/kJmol$^{-1}$')
plt.xlabel(r'$\phi$/rad')
plt.tight_layout()
plt.savefig('dihedral.pdf')
plt.close()
