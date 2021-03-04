import numpy as np
from math import sin


def num_integral(func, a, b):
    res = []
    for i in range(0, 20):
        N = 2**(i)
        s = 0
        for j in range(1, N+1):
            s += func(a + ((j-1/2))*(b-a)/2)

        res.append(((b-a)/N)*s)

    return res


y = num_integral(lambda x: sin(x), 0, 6.2832)

for i in y:
    print(i)
