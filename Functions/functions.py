import os
from os import system
from math import pow
from time import sleep 

system('cls')

# print()
print('Hi how are you?')

# user-defined function

def add(n1, n2):
    result = n1 + n2
    return result

def subtract(n1, n2):
    result = n1 - n2
    return result

def multiply(n1, n2):
    result = n1 * n2
    return result

def divide(n1, n2):
    result = n1 / n2
    return result

def findModulus(n1, n2):
    result = n1 % n2
    return result

def findExponent1(n1, n2):
    result = n1 ** n2
    return result

def findExponent2(n1, n2):
    result = pow(n1, n2)
    return result

# Accept input from the user
num1 = int(input("Enter first number >> "))
num2 = int(input("Enter second number >> "))

# function calls 1
addition = add(num1, num2)
subtraction = subtract(num1, num2)
multiplication = multiply(num1, num2)
division = divide(num1, num2)
modulus = findModulus(num1, num2)
exponent1 = findExponent1(num1, num2)
exponent2 = findExponent2(num1, num2)
# ---------------------------

# print function results
print(f"The result returned by the add() function is {addition}")
print(f"The result returned by the subtract() function is {subtraction}")
print(f"The result returned by the multiply() function is {multiplication}")
print(f"The result returned by the divide() function is {division}")
print(f"The result returned by the findModulus() function is {modulus}")
print(f"The result returned by the findExponent1() function is {exponent1}")
print(f"The result returned by the findExponent2() function is {exponent2}")
print()

# function call 2
print(f"The result returned by the add() function is {add(num1, num2)}")
print(f"The result returned by the subtract() function is {subtract(num1, num2)}")
print(f"The result returned by the multiply() function is {multiply(num1, num2)}")
print(f"The result returned by the divide() function is {divide(num1, num2)}")
print(f"The result returned by the findModulus() function is {findModulus(num1, num2)}")
print(f"The result returned by the findExponent1() function is {findExponent1(num1, num2)}")
print(f"The result returned by the findExponent2() function is {findExponent2(num1, num2)}")


sleep(5)
system('cls')
def printPersonInfo(fname, lname, age, phoneNum, PIN, school): 
    print(f'''
    First Name:................... {fname}
    Last Name:.................... {lname}
    Age:.......................... {age}
    Phone #:...................... {phoneNum}
    PIN:.......................... {PIN}
    School:....................... {school}
    ''')

print('********** Multiple Values for Function ***********')
fname = input("Enter your first name >> ")
lname = input("Enter your last name >> ")
age = int(input("Enter your age >> "))
phone = input("Enter your phone number >> ")
pin = int(input("Enter your PIN number >> "))
school = input("What is your school? >> ")

# call function printPersonInfo
printPersonInfo(fname, lname, age, phone, pin, school)
