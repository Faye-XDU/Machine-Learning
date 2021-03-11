import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)

y = 1 / (1 + np.exp(-x))
z = x**2
plt.xlim(-2,2)
plt.ylim(0,1)

plt.plot(x, y, color='#E0BF1D', linestyle='-', label="sigmoid")
plt.plot(x, z, color='purple', linestyle='-.', label="y=x*x")

plt.legend(loc="upper left")

plt.show()