import numpy as np 
import matplotlib.pyplot as plt
import abspath
from velfield import velfield

# Local pypackage that I created to easily access the absolute path of some selected directories.
path = abspath.get_path("MEK1100") + "/Oblig1/images"

# Chose an odd number to include the point in the middle where ther is no flow.
n_val = 11

# Gets values x, y, u and v, then plots them into the vector field.
x, y, u, v = velfield(n_val)
plt.quiver(x, y, u, v)
plt.title(f"Vector field with n={n_val}")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.savefig(f"{path}/vec_{n_val}.png")