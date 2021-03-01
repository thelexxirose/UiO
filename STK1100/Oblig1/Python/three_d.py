# Import the function created in three_c.py
import numpy as np
from three_c import Fx_px

# Execute the function and store Fx and px as variables
Fx, px = Fx_px()

# Create funhction that calculate


def h(X): return (100000/1.03**32) * (1 - (1/1.03)**(X-31))/(1 - (1/1.03)) if X >= 32 else 0


# Create arange from 0 to including 71
arr = np.arange(72)

# Map through arr and apply the function h to every element. Should return 0 on the 32 first elements.
hx = np.array(list(map(h, arr)))

# Sum of the product of each element in hx and px
Ex = sum(hx*px)

print(Ex)

'''
cory@Nickelback:~/Documents/UiO/STK1100/Oblig1$ /usr/bin/python3 /home/cory/Documents/UiO/STK1100/Oblig1/Python/three_d.py
501511.92449024785
'''
