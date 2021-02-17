import math

def for_form(n, a_1, a_0):
    s = 0
    for i in range(n+1):
        if i == 1 or i == 0:
            s = 1.0
        else:
            s = 4.0*a_1 + a_0
            res_0 = a_0
            res_1 = a_1
            a_0 = a_1
            a_1 = s
    return [s, res_1, res_0]

print("Initial conditions: a_0 = 1, a_1 = 2 - sqrt(5) \n")

for i in range(2, 101):
    f = for_form(i, 2.0 - math.sqrt(5.0), 1.0)
    print(f"n = {i:3d}: 4*a_{i-1} = {4*f[1]:>24} <==> a_{i-2} = {f[2]:>24} <==> 4*a_{i-1} + a_{i-2} = {f[0]:>24}")