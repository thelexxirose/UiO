from Euler import Euler

import matplotlib.pyplot as plt
import numpy as np
from numpy import cos

eq = Euler(0, 1, lambda x, y: y * (0.5 - y))

eq.plot("forward euler", [0, 3], 6)


def analytic(x): return -1/(np.exp(-x/2) - 2)


x = np.linspace(0, 3, 101)
y = np.vectorize(analytic)

plt.plot(x, y(x), label="analytic")
plt.legend()
plt.savefig("images/task_2b.png")

eq.plot("midpoint euler", [0, 3], 6)

plt.legend()
plt.savefig("images/task_2c.png")
plt.show()
