import math

def for_form(n, a_1, a_0):
    s = 0
    for i in range(n+1):
        if i == 1 or i == 0:
            s = 1.0
        else:
            s = 4.0*a_1 + a_0
            a_0 = a_1
            a_1 = s
    return s

print("Initial conditions: a_0 = 1, a_1 = 2 - sqrt(5) \n")

for i in range(2, 101):
    f = for_form(i, 2.0 - math.sqrt(5.0), 1.0)
    print(f"n = {i:3d}: {f:>24}")