from scipy.integrate import quad
import math as m


def integral(start, end):
    return m.sqrt(0.5*((m.atan(end))**2) - 0.5*((m.atan(start))**2))


for i in range(20):
    print(f"{i}: {quad(lambda x: m.sqrt(m.atan(x)/(1+x**2)), i, i+1)}, {integral(i, i+1)}")
