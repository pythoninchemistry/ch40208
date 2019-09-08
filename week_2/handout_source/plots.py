import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
y = x ** 2

plt.plot(x, y)
plt.savefig('x_squared.pdf')
