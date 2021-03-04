import numpy as np 
import matplotlib.pyplot as plt

k = 500     # spring constant in N/m
h = 0.3     # height difference between block and "floor", in m
x0 = 0.4    # nautral position on x-axis, in m
x1 = 0.65    # draging the block to a start position on x-axis, in m
L0 = 0.5    # spring length in nautral position, in m
m = 5       # block weight, in kg

time = 10       # Time window
dt = 0.001      # Time intervals

n = int(np.ceil(time/dt))

# Defining the arrays:
t = np.zeros(n,float)
r = np.zeros(n,float)
v = np.zeros(n,float)
a = np.zeros(n,float)

# Here we use the initial conditions for the first vector elements
r[0] = x1 	# at the start, the person is at x = 0
t[0] = 0.0	# We start the clock at t = 0 s
v[0] = 0.0	# no velocity at the start, v0 = 0 m/s
a[0] = 0.0  # at the start, the speed = 0

# Now we calculate everything 
for i in range(n-1):
	# calculating the force in x-direction
	Fx = -k*(r[i]-x0)*(1-(L0/np.sqrt(r[i]**2+h**2))) 
	# calculating the acceleration:
	a[i] = Fx/m 

	# Calculating with the Euler-Cromer method:
	v[i+1] = v[i] + a[i]*dt
	r[i+1] = r[i] + v[i+1]*dt
	t[i+1] = t[i] + dt

# In the first "window", we plot how the position x evolves with time
plt.subplot(2,1,1)
plt.plot(t,r)
plt.xlabel('Time t [s]')
plt.ylabel('Position x [m]')

# Now switch to the next "window", index = 2
# Here we want to plot how the velocity v varies with time t
plt.subplot(2,1,2)
plt.plot(t,v, 'r')
plt.xlabel('Time t [s]')
plt.ylabel('Velocity v [m/s]')

# Show everything:
plt.show()