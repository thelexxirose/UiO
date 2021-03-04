import numpy as np 
import matplotlib.pyplot as plt

k = 500     # spring constant in N/m
L0 = 0.5    # spring length in m
h = 0.3     # height in m

# Created a linspace that goes from the bounds defined by the task
x = np.arange(-0.75, 0.75, 0.05)

# Defined F_x function
F_x = -k*x*(1-(L0/np.sqrt(x**2+h**2)))

print(F_x)

plt.plot(x, F_x)
plt.xlabel("Position x [m]")
plt.ylabel("Force in x-direction given position x [N]")
plt.show()