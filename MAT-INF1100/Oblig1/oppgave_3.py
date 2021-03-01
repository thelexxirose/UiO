from random import random

antfeil = 0
N = 100000

for i in range(N):
    x = random()
    y = random()
    z = random()
    res1 = (x + y) * (y + z)
    res2 = x*y + y*y + x*z + y*z
    if res1 != res2:
        antfeil += 1
        x0 = x
        y0 = y
        z0 = z
        ikkelik1 = res1
        ikkelik2 = res2

print(100.*antfeil/N)
print(x0, y0, z0, ikkelik1 - ikkelik2)
