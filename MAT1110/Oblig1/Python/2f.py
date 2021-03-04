import numpy as np
import matplotlib.pyplot as plt

# Function that plots a figure with different a,b,c
# values and output a png file


def plot(a, b, c, name, density):
    plt.clf()

    skip = (slice(None, None, density), slice(None, None, density))

    plt.quiver(x[skip], y[skip], (a*x + b*y)[skip], (c*x - a*y)[skip])
    plt.contour(x, y, c*x**2 - 2*a*x*y - b*y**2, 32)
    plt.axis('equal')
    plt.title(f"a={a}, b={b}, c={c}")
    plt.savefig(f"/home/cory/Documents/UiO/MAT1110/Oblig1/images/{name}.png")


# Make a linspace to be used for the meshgrid
dim = np.linspace(-30, 30, 1001)

# Create a meshgrid that spans from -30 to 30 in both the x and y directions
x, y = np.meshgrid(dim, dim)

# Plot different contour graphs where a,b and c are chosen so that
# -(a^2 + bc) > 0 and -(a^2 + bc) < 0
plot(2, -2, 3, "ellipse", 50)
plot(2, 2, 3, "hyperbolic", 50)
