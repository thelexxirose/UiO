import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1001)


def r(t): return (t**2, t**3)


plt.plot(r(t)[0], r(t)[1])

plt.show()
