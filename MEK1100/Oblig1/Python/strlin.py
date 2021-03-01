import numpy as np 
import matplotlib.pyplot as plt
from streamfun import streamfun
import os

# Accessing an environment variable that points to the MEK1100 directory
path = f"{os.getenv('MEK1100')}/Oblig1/images"

# different values of n
n_vals = [5, 30]

# loops through different values for n and outputs .png files
for i in n_vals:
    x, y, psi = streamfun(i)
    plt.clf()
    plt.contour(x, y, psi)
    plt.title(f"Streamlines with n={i}")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig(f"{path}/strlin_{i}.png")