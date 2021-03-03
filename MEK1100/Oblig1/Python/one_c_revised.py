import numpy as np 
import matplotlib.pyplot as plt
import os

# Accessing an environment variable that points to the MEK1100 directory
img_path = f"{os.getenv('MEK1100')}/Oblig1/images"

# function that plots x*, y* with t* and different values for theta
def plot(theta):
    t_star = np.linspace(0,1,101)

    x_star = lambda t, theta: t
    y_star = lambda t, theta: t*(np.tan(theta)) - (t**2*np.tan(theta))

    plt.plot(x_star(t_star, theta), y_star(t_star, theta), label=f"Theta={theta:.3f}")


# List of different valuesof theta
theta_list = [np.pi/3, np.pi/4, np.pi/6]

for i in theta_list:
    plot(i)
    plt.legend()
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig(f"{img_path}/one_c_revised.png")