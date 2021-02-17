from Approx import Approx

f_1 = Approx(lambda x: x**2 - 4, [0,5])

print(f_1.approximate())
