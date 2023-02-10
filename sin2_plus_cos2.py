# a
from math import sin, cos, pi

x = pi/4
value = sin(x)**2 + cos(x)**2
print(value)

# b
v = 3  # m/s
t = 1  # s
a = 2  # m/s/s
s = (v * t) + (0.5 * a * (t ** 2))
print(s)

# c
a = 3.3
b = 5.3
a_2 = a ** 2
b_2 = b ** 2

eq1_sum = a_2 + 2 * a * b + b_2
eq2_sum = a_2 - 2 * a * b + b_2
eq1_pow = (a + b) ** 2
eq2_pow = (a - b) ** 2

print(f'first equation: {eq1_pow}={eq1_sum}')
print(f'second equation: {eq2_pow}={eq2_sum}')
