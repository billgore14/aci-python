import os 
from os import system
system('cls')


# TUPLE
#index    0   1   2   3   4   5   6   size - 1
array = ( 87, 10, 2, 46, 22, 19, 66)
# size    1    2   3  4   5   6  7   size 7

print(type(array))

print(array)

for number in array:
    print(number)


# LIST 
cars = ["BWM", "Toyota", "Mercedes"]
print(cars)
print(type(cars))

cars.sort()

for car in cars:
    print(car)


numbers = [6, 3, 8, 1, 2, 8, 3]
print("Before sorting list")
for n in numbers:
    print(n)
print()
print("After sorting the list")
numbers.sort()
for n in numbers:
    print(n)
    
