import numpy as np
import matplotlib.pyplot as plt 

t = np.linspace(0, 6*np.pi, 1001)

r = lambda t: (t*np.cos(t), t*np.sin(t)) 

print(r(t))

plt.plot(r(t)[0], r(t)[1])

plt.show()