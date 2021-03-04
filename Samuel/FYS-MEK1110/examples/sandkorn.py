# Python script
# Grain of sand falling through water until it reaches the bottom
# Cecilie
# Last update: Jan 14, 2021
# a.c.larsen@fys.uio

# Import Python libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the variables
a0   = 6.2 # m/s^2
c    = 1.8 # s^(-1)
time = 2.0 # s
dt   = 0.001 #s

# Here using the numpy ceil funtion to get the number of array elements
# The ceil of a scalar b is the smallest integer i such that i>= b
# https://www.geeksforgeeks.org/numpy-ceil-python/
n = int(np.ceil(time/dt))

# Print it to screen
print(' Number of array elements: ',n)

# Define the arrays we need for the time t, position x, velocity v, and acceleration a
t = np.zeros(n,float)
x = np.zeros(n,float)
v = np.zeros(n,float)
a = np.zeros(n,float)

# Initial conditions to be set for the first array elements
x[0] = 2.0 # m
t[0] = 0.0 # s
v[0] = 0.0 # m/s

# Initialize the loop index
i=0

# Set up the while loop to calculate the acceleration, velocity and position
# We need the loop index to be smaller than the number of array elements,
# and we need the position x to always be positive as we have defined 
# the bottom at x=0
# Again we are using the Euler-Cromer method
while i<n-1 and x[i]>0:
	a[i]   = -a0 -c*v[i]
	v[i+1] = v[i] + a[i]*dt
	x[i+1] = x[i] + v[i+1]*dt
	t[i+1] = t[i] + dt
	i      = i + 1 
	# Print values of the whole time array
	#print('t=%.3f' % t[i])

# Print values of the last element in the time array,
# i.e. the last time step at which x[i] is still positive: 
print('t=%.3f' % t[i])

# Now we want to plot things again.
# Make space for three rows (nrows = 3), one column (ncols = 1), index = 1; 
# the index starts at the left upper corner and increases to the right 
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
# In the first "window", we plot how the position x evolves with time
plt.subplot(3,1,1)

# We want to show only the parts of the arrays that 
# actually have values, that means up to the last step
# at which x[i] is positive:
plt.plot(t[0:i],x[0:i])

# Put nice axis titles so we know what we are looking at! Remember units!
plt.xlabel('t [s]')
plt.ylabel('x [m]')

# Now switch to the next "window", index = 2
# Here we want to plot how the velocity v varies with time t
plt.subplot(3,1,2)
plt.plot(t[0:i],v[0:i])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')

# Finally we plot the acceleration a as a function of time t
# in the third "window" (index = 3)
plt.subplot(3,1,3)
plt.plot(t[0:i],a[0:i])
plt.xlabel('t [s]')
plt.ylabel('a [m/s$^2$]') # For those of you who have seen LaTeX, the dollars are familiar :)

# Now, we want to show everything:
plt.show()
#ta-daaaa !!!

