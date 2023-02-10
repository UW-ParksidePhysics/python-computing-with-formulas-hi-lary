# cook the perfect egg
from math import log, pi

m = eval(input('egg mass in grams:'))  # mass of egg g
p = 1.038  # density of egg g/cm/cm/cm
c = 3.7  # heat capacity J/g/K
k = 5.4 * 10**-3  # thermal conductivity of egg W/cm/K
Tw = 100  # temp of water Celsius
Ti = eval(input('initial temperature of egg in celsius:'))  # initial temp of egg celsius
Ty = 70  # cooked yolk temp Celsius

time = (m**(2/3)*c*p**(1/3))/(k*pi**2*((4*pi)/3)**(2/3))*log(0.76*((Ti-Tw)/(Ty-Tw)))  # seconds

print(f'Given a {m}g egg at an initial temperature of {Ti}C, it will take {time} seconds to cook the yolk.')
