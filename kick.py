# air resistance
from math import pi
q = 1.2  # air density kg/m/m/m
g = 9.81  # acceleration due to gravity m/s/s
Cd = 0.2  # drag coefficient
r = 0.11  # radius of ball m
A = pi*r**2  # area of ball w radius r m**2
m = 0.43  # mass kg
v = eval(input('kick velocity km/h:'))  # velocity of kick km/h

V = v * 1/60 * 1/60 * 10 ** 3
Fd = 0.5 * Cd * q * A * V**2  # drag force N
Fg = m * g  # gravity force N
Fr = Fd/Fg  # force ratio


print(f'Given a kick velocity, the drag force is {Fd}N and the gravity force is {Fg}N.')
print(f'This yields a ratio of {Fr}')


