import matplotlib.pyplot as plt
import math
import cmath

Z_west = (0, 0)
Z_east = (1, 0)
Z_g = (0.3, 0.25)

VZ_gw = cmath.polar(complex(Z_g[0] - Z_west[0], Z_g[1] - Z_west[1]))
VZ_ge = cmath.polar(complex(Z_g[0] - Z_east[0], Z_g[1] - Z_east[1]))

rot_ext = cmath.rect(1, cmath.pi/3)
rot = cmath.e**complex(0, -(cmath.pi/4))

W_west = VZ_gw[0] * cmath.exp(VZ_gw[1]) * rot_ext
W_east = 1 * rot

print(rot_ext)


#plt.plot([Z_west[0], Z_east[0], W_west.real, W_east.real], [Z_west[1], Z_east[1], W_west.imag, W_east.imag], 'ro')

#plt.show()