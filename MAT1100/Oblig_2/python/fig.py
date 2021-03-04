import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 101)
def y(x): return x**2


plt.plot(x, y(x))
plt.show()
