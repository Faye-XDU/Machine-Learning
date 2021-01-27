import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = 1 / (1 + np.exp(-x))
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(-5, 5)
plt.ylim(-1.2, 1.2)
plt.title("sigmoid function")
plt.grid(linestyle=":", color="red")
plt.axhline(y=0.5, color="green", linestyle="--", linewidth=2)
plt.axvline(x=0.0, color="green", linestyle="--", linewidth=2)
plt.plot(x, y)
plt.show()
