from matplotlib import pyplot as plt


def f(x, y): return [x**2, x*y, y**2]


width_of_panel = 4
height_of_panel = 3

d = 1000

plt.figure(figsize=(width_of_panel, height_of_panel), dpi=d)
