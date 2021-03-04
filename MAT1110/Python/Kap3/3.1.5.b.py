import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1001)


def r(t):
    return (5*np.cos(t), 3*np.sin(t))


plt.plot(r(t)[0], r(t)[1])

plt.show()
