import math

f = lambda x: math.exp(x**2)

s = 0

for i in range(4):
    s += f(i/2) + f((i+1)/2)


print(s/4)