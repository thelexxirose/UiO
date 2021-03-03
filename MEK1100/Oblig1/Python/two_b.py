import numpy as np
import matplotlib.pyplot as plt
import os

# Accessing an environment variable that points to the MEK1100 directory
path = f"{os.getenv('MEK1100')}/Oblig1/images"


def mesh_grid(start, stop, dt):
    # Create a linspace
    I = np.linspace(start, stop, dt)

    # Create a meshgrid that uses the linspace dimensions
    x, y = np.meshgrid(I, I)

    return x, y


def vec_field(x, y, u, v, density):
    # Variable that tells how much to divide the number of elements in the mesh by.
    skip = (slice(None, None, density), slice(None, None, density))

    # Returns the vectorfield with the correct density.
    return u[skip], v[skip], skip


def streamlines(x, y, func):
    # Returns a meshgrid
    return func


if __name__ == "__main__":
    x, y = mesh_grid(-10, 10, 1000)

    u, v, skip = vec_field(x, y, x*y, y, 120)

    f = streamlines(x, y, y - np.log(abs(x)))

    plt.quiver(x[skip], y[skip], u, v)
    plt.contour(x, y, f, 6)
    plt.axis('equal')
    plt.title("Task 2B")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig(f"{path}/two_b.png")
