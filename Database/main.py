import os 
from os import system 
import operations as ops
from colorama import Fore, Style

system('cls')

operationList = ["Read", "Insert", "Update", "Delete"]
counter = 1

print("These are the operations that you can perform in our database: ")
for operation in operationList:
    print(Fore.RED, f'{counter}. {operation}', Style.RESET_ALL)
    counter += 1
choice = int(input("Select one above [1-4] >> "))

if choice == 1:
    ops.readUserOperation()
elif choice == 2:
    ops.insertOperation()

    

print()
