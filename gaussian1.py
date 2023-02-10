# gaussian

from math import sqrt, pi, e

m = 0
s = 2
x = 1
gauss = (1 / (sqrt(2 * pi) * s)) * e**((-1 / 2) * ((x - m) / s) ** 2)

print(gauss)
