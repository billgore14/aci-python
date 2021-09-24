import os, datetime 
from os import system 
from datetime import datetime

system('cls')

username = "carlos"
password = "pass"
path = './Functions/log.txt'

user = input("Enter username >> ")
passwd = input("What is your password? >> ")

def printSuccessOrFail(message):
    if message == "Success":
        with open(path, 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}') 
            log.close()
    else:
        with open(path, 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')

if (user == username and password == passwd):
    print(f'Hello, {user}, you are fully authenticated')
    printSuccessOrFail("Success")
else:
    print("The combination of the username and password you used does not match our records")
    printSuccessOrFail("Fail")