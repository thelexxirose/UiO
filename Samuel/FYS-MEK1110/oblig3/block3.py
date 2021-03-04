import numpy as np 
import matplotlib.pyplot as plt

k = 500     # spring constant in N/m
h = 0.3     # height difference between block and "floor", in m
x0 = 0.4    # nautral position on x-axis, in m
x1 = 0.75   # draging the block to a start position on x-axis, in m
L0 = 0.5    # spring length in nautral position, in m
m = 5.0     # block weight, in kg
g = 9.81	# gravity in m/s^2
uD = 0.05   # friction coffiecient

time = 10       # Time window
dt = 0.001      # Time intervals

n = int(np.ceil(time/dt))

# Define the arrays we need for the time t, position x, velocity v and acceleration a
t = np.zeros(n,float)
x = np.zeros(n,float)
v = np.zeros(n,float)
a = np.zeros(n,float)

# Here we use the initial conditions for the first vector elements
x[0] = x1 	# at the start, the person is at x = 0
t[0] = 0.0	# We start the clock at t = 0 s
v[0] = 0.0	# no velocity at the start, v0 = 0 m/s
a[0] = 0.0  # at the start, the speed = 0

# Now we calculate everything 
for i in range(n-1):
	Fx = -k*(x[i]-x0)*(1-(L0/np.sqrt(x[i]**2+h**2)))  # calculating the force in x-direction
	N = k*h*(1-(L0/np.sqrt(x1**2+h**2)))+m*g		# calculating the nautral force

	# if statement to check wich way the block is moving and add the friction in the oppisite direction
	if v[i] >= 0:
		u = np.sqrt(N**2) * uD
	if v[i] <= 0:
		u = np.sqrt(N**2) * (-uD)

	Fnet = Fx-(u)
	a[i] = Fnet/m # calculating the acceleration:
	# Calculating the velocity and the position with the Euler-Cromer method:
	v[i+1] = v[i] + a[i]*dt
	x[i+1] = x[i] + v[i+1]*dt
	t[i+1] = t[i] + dt

# calculating the kinetric energy throughtout the movement:
E_kin = (1/2)*m*v**2

# In the first "window", we plot how the position x evolves with time
plt.subplot(3,1,1)
plt.plot(t,x)
plt.xlabel('Time t [s]')
plt.ylabel('Position x [m]')

# Now switch to the next "window", index = 2
# Here we want to plot how the velocity v varies with time t
plt.subplot(3,1,2)
plt.plot(t,v, 'r')
plt.xlabel('Time t [s]')
plt.ylabel('Velocity v [m/s]')

plt.subplot(3,1,3)
plt.plot(x, E_kin, 'g')
plt.ylabel('Kinetric energy Joule [J]')
plt.xlabel('position x [m]')
# Show everything:
plt.show()
