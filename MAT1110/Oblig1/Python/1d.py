import numpy as np 
import matplotlib.pyplot as plt

# Used a and b values from the task
a = 1
b = 3

# Created a linspace that goes from the bounds defined by the task
t = np.linspace(-b, b, 1001)

# Defined r(t) as a lambda function taht returns a tuple
r = lambda t: (a*np.arcsinh(t/a), np.sqrt(a**2 + t**2))

# plot r(t)
plt.plot(r(t)[0], r(t)[1])
plt.savefig("./images/1d.png")