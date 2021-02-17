
import numpy as np 
import matplotlib.pyplot as plt

m = 80      # massen til sprinteren
k = 400     # kreftene sprinteren bruker for å komme opp i fart
v0 = 0.0    # startsfarten

#Konstantene i beregningen av luftmotstanden D:
P = 1.293	#kg/m^3
Cd = 1.2	#air density kg/m³
A_0 = 0.45	#Areal overflaten til sprinteren m^2
w = 0.0		#Farten til vinden
v = 100/9.58 	#Farten ved 100m

D = 0.5 * P * Cd * A_0 * (v - w)**2		#Luftmotstanden D

time = 12  # sekunder
dt = 0.01    # antal intervaler vi måler tiden med
t = np.arange(0, time, dt) # fordeller tiden fra 0 til tid med intervalet dt
n = len(t)  # lengden til t: altså antall punkter

# alle ting som varierer med t:
s = np.zeros(n)     # avtsanden/strekning
v = np.zeros(n)     # farten til sprinteren
F = np.zeros(n)     # samlede krefter på sprinteren
a = np.zeros(n)     # akselerasjonen til sprinteren

# Initialverdiene:
s[0] = 0
v[0] = v0
F[0] = k - D
a[0] = F[0]/m

# Euler-cromers:
for i in range(0, n-1):
    F[i+1] = -F[i] * s[i] - m * a[i] #Cory: Shouldn't it be F[i] and a[i] instead of F[0] and a[0]? 
    a[i+1] = F[i]/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i+1]*dt

#Plotting the sprinters position, velocity and accelaration
fig, axs = plt.subplots(3)
fig.suptitle('100m Sprinter')
#Cory: Switched what variable goes to which axis, so that time corresponds with the x axis
axs[0].plot(s, t)
axs[1].plot(v, t)
axs[2].plot(a, t)
axs[0].set_xlabel('s (m)')
axs[1].set_xlabel('v (m/s)')
axs[2].set_xlabel('a (m/s^2)')
axs[0].set_ylabel('t (sek)')
axs[1].set_ylabel('t (sek)')
axs[2].set_ylabel('t (sek)')

plt.show()