# FYS-MEK 1110
# The bungee jump example from Andreas Goergen's
# lecture on January 28, 2020
# A tough girl or guy is jumping off a bridge
# doing a bungee jump.
# The question is whether this brave person
# is going to touch the ground or not (we hope not!)
# This is such a complex problem that it must be solved numerically.
# The forces are: gravity, air resistance and the force
# from the bungee (i.e. the elastic cord)
# See also drawing from the lecture
# Positive direction is defined as upward (opposite of graviational-force direction)
# Cecilie, 3 Feb 2020
# Last update: 21 Jan 2021
# a.c.larsen@fys.uio.no

# Import nice Python libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the constants and variables we need
g = 9.81 	# tyngdeakselerasjon i m/s^2
D = 0.8		# luftmotstandskoeffisient i kg/m
m = 70.		# masse i kg
k = 40.		# fjaerkonstant i N/m
h = 100.  # broas hoeyde i m
d = 50.		# strikkens lengde i m ved likevekt (ikke strukket eller kroellet opp)
time = 60.  # maximum tid vi ser paa i sekunder
dt = 0.001  # tidssteg i sekunder

# Here we are using the numpy ceil funtion to get the number of array elements
# we want to use for the arrays.
# The ceil of a scalar b is the smallest integer i such that i>= b
# https://www.geeksforgeeks.org/numpy-ceil-python/
n = int(np.ceil(time/dt))

# Define the arrays we need for the time t, position x, velocity v, and acceleration a
t = np.zeros(n, float)
x = np.zeros(n, float)
v = np.zeros(n, float)
a = np.zeros(n, float)

# Here we use the initial conditions for the first vector elements
x[0] = h 	# at the start, the person is at the top of the bridge
t[0] = 0  # We start the clock at t = 0 s
v[0] = 0  # no velocity at the start, v0 = 0 m/s

# Now we are ready to calculate everything
# We must be careful with the signs -> directions of movement
# and directions of the forces!
for i in range(0, n-1):
    # First we calculate the force from the bungee:
    if x[i] < (h-d):  # the position is below the equilibrium point, so the bungee is stretched
        Fk = k*(h-d-x[i])  # the force from the bungee acts upwards, so in the *positive* direction
    else:
        Fk = 0.  # if the position is at equilibrium or above, there is no force from the bungee
    # Now we calculate the air resistance.
    # Here we must be careful to ensure
    # that it always works against the direction of motion!
    # Therefore, we use the trick of describing it with the term
    # v[i]*abs(v[i]) instead of just v[i]**2, which would have made another if-test necessary
    Fd = -D*v[i]*abs(v[i])
    # The gravitational force, defined as working in the negative direction
    Fg = -m*g
    # Now that we have all the force components, we can use Newton's 2nd law
    # and calculate the acceleration:
    a[i] = (Fk + Fd + Fg)/m
    # Finally, we get to the equations of motion
    # to calculate the velocity and the position
    # with the Euler-Cromer method:
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt
    t[i+1] = t[i] + dt

# Now it's time to plot everything and check the position:
# will the person crash into the ground or not??
# Make space for three rows (nrows = 2), one column (ncols = 1), index = 1;
# the index starts at the left upper corner and increases to the right
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
# In the first "window", we plot how the position x evolves with time
plt.subplot(2, 1, 1)
plt.plot(t, x)

# Put nice axis titles so we know what we are looking at! Remember units!
plt.xlabel('Tid t [s]')
plt.ylabel('Posisjon x [m]')

# Now switch to the next "window", index = 2
# Here we want to plot how the velocity v varies with time t
plt.subplot(2, 1, 2)
plt.plot(t, v)
plt.xlabel('Tid t [s]')
plt.ylabel('Hastighet v [m/s]')

# Show everything
plt.show()
