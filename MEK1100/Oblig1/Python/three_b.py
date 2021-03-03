import numpy as np
import matplotlib.pyplot as plt
import os

# Accessing an environment variable that points to the MEK1100 directory
path = f"{os.getenv('MEK1100')}/Oblig1/images"

if __name__ == "__main__":

    # Since we are dealing with only the x-axis and y-axis,
    # there is no need to have a mesh grid.
    # we can make an array containing only zeros, and one
    # with values and use those to plot vectors in a field.
    zeros = np.zeros(11)
    vals = [2*i for i in range(-10, 11, 2)]

    # Defining u and v
    u = lambda x,y: np.cos(x)*np.sin(y)
    v = lambda x,y: -np.sin(x)*np.cos(y)

    # Plot the vectors on the axes.
    plt.quiver(zeros, vals, u(zeros, vals), v(zeros,vals))
    plt.quiver(vals, zeros, u(vals, zeros), v(vals,zeros))
    plt.axis('equal')
    plt.title("Task 3B")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig(f"{path}/three_b.png")
