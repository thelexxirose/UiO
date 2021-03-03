import numpy as np 
import matplotlib.pyplot as plt
import os

img_path = f"{os.getenv('MEK1100')}/Oblig1/images"

def plot(theta):
    t_star = np.linspace(0,1,101)

    x_star = lambda t, theta: t
    y_star = lambda t, theta: t*(np.sin(theta)/np.cos(theta)) - t**2 * (np.cos(theta)/np.sin(theta))

    plt.plot(x_star(t_star, theta), y_star(t_star, theta), label=f"Theta={theta:.3f}")

theta_list = [np.pi/3, np.pi/4, np.pi/6]

for i in theta_list:
    plot(i)
    plt.legend()
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig(f"{img_path}/one_c_revised.png")