import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
y = x ** 2

plt.plot(x, y)
plt.savefig('x_squared.pdf')
plt.close()

temperature = np.linspace(283, 363, 10)
rate_constants = np.array([3.2e-19, 3.4e-18, 3.2e-17, 2.6e-16,
                           1.8e-15, 1.2e-14, 7.3e-14, 3.9e-13,
                           1.9e-12, 8.9e-12])
rate_constants_uncertainity = np.array([1.6e-20, 1.7e-19, 1.6e-18, 1.3e-17,
                           9.4e-17, 6.2e-16, 3.7e-15, 2.0e-14,
                           1.0e-13, 4.4e-13])

plt.errorbar(temperature, rate_constants*10**12, rate_constants_uncertainity*10**12, marker='o', linestyle='')
plt.ylabel(r'Rate constant/$\times10^{-12}$ s$^{-1}$')
plt.xlabel(r'Temperature/K')
plt.title(r'Effect of temperature of rate constant of HI decomposition')
plt.tight_layout()
plt.savefig('real.pdf')
plt.close()
