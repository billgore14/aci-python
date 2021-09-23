import os
from os import system
from math import pow
from time import sleep

system('cls')


print('''

    6 > 5 = {}
    4 > 5 = {}
    10 >= 5 = {}
    5 >= 5 = {}
    6 <= 5 = {}
    6 != 5 = {}
   
    
    
    '''.format(
        6 > 5, 
        4 > 5,
        10 >= 5,
        5 >= 5,
        6 <= 5,
        6 != 5))

x = 2
x += 1 # += is the same as x = x + 1
print("The value of x using += is {}".format(x))
print()
x -= 1  # += is the same as x = x - 1
print("The value of x using -= is {}".format(x))
print()
x *= 2  # += is the same as x = x * 2
print("The value of x using *= is {}".format(x))
print()
x /= 2  # += is the same as x = x / 2
print("The value of x using /= is {}".format(x))
x += 9
print()
print("The current value of x is {}".format(x))
print()
x %= 2
print("The value of x using %= is {}".format(x))
print()

x = x + 1
x+=2 # x = x + 2