# Python script for "The Rocket"
# Cecilie, Jan 21, 2020
# Last update: Jan 14, 2021
# a.c.larsen@fys.uio

# Import Python libraries
import numpy as np
import matplotlib.pyplot as plt

# Make 1D arrays for the time and acceleration,
# and fill with the data from the text file.
# The unpack=True argument tells the function loadtxt() that
# the file contains columns of data that should be put in the
# separate arrays t and a
t, a = np.loadtxt('therocketdata.txt', usecols=[0, 1], unpack=True)

# Define the time step as the difference between
# the first two elements in the time array
# (this works because the time steps are constant in the file)
dt = t[1] - t[0]

# Find the length of the time array, i.e. how many elements (data points) we have
n = len(t)

# Now we can make arrays for the position and velocity as well,
# with the same size as the time and acceleration arrays, obviously.
# We initialize these array elements with zeros and will calculate them later
x = np.zeros(n, float)
v = np.zeros(n, float)

# Initial conditions to be set for the first array elements of the position and velocity
x[0] = 0.0
v[0] = 0.0

# Now we want to make a loop to calculate the velocity and position
# based on the data we have for the acceleration.
# For this, we use the equations of motion
# and the Euler-Cromer method
for i in range(0, n-1):
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt  # note the v[i+1] term; if it would be v[i] it would be the Euler method

# Now we want to plot things and look at the stuff
# Make space for three rows (nrows = 3), one column (ncols = 1), index = 1;
# the index starts at the left upper corner and increases to the right
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
# In the first "window", we plot how the position x evolves with time
plt.subplot(3, 1, 1)
plt.plot(t, x)

# Put nice axis titles so we know what we are looking at! Remember units!
plt.xlabel('t [s]')
plt.ylabel('x [m]')

# Now switch to the next "window", index = 2
# Here we want to plot how the velocity v varies with time t
plt.subplot(3, 1, 2)
plt.plot(t, v)
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')

# Finally we plot the acceleration a as a function of time t
# in the third "window" (index = 3)
plt.subplot(3, 1, 3)
plt.plot(t, a)
plt.xlabel('t [s]')
plt.ylabel('a [m/s$^2$]')  # For those of you who have seen LaTeX, the dollars are familiar :)

# Now, we want to show everything:
plt.show()
# ta-daaaa !!!
