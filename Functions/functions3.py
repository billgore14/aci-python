import os 
from os import system 

system('cls')

def printName():
    print("My name is Charles")

def printInfo(name, age):
    print(f"My name is {name} and I am {age} years old")

def printInfoNoArgs():
    return "I am happy here"

def printInfoWithArgs(price):
    tax = price * .07
    subtotal = price
    grandTotal = price + tax
    return tax, subtotal, grandTotal


printName()
printInfo("Charles", 40)
string = printInfoNoArgs()
print(string)

print(printInfoNoArgs())

t, sbtotal, grTotal = printInfoWithArgs(25999)
print(f'''
    Subtotal:........ ${sbtotal}
    Taxes:........... ${t}
    Grand Total...... ${grTotal}
''')
