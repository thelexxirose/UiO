import numpy as np 
import matplotlib.pyplot as plt

I = np.linspace(-10, 10, 21)

x, y = np.meshgrid(I, I)

plt.quiver(x, y, x*y, y)

plt.contour(x, y, y - np.log(abs(x)), 8)

plt.axis('equal')

plt.show()