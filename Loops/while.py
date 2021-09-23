import os
from os import system
from time import sleep

system('cls')


counter = 0
hiCounter = 1

while counter < 10:
    # when counter = 10, then the boolean expression counter < 10 becomes false, then it exits the loop
    print(f"{hiCounter}.Hi")
    counter += 1
    hiCounter += 1

sleep(3)
system('cls')


attemptCounter = 3
name = input("What is your name? >> ")
while True:
    print(f"Ok, {name}, you have {attemptCounter} attempts to login")
    input('Login >> ')
    if(attemptCounter == 1):
        break
    print(f"You have {attemptCounter - 1} attempts")
    attemptCounter -= 1
print("Your account has been locked. Call Customer Service for assistance to unlock your account")


while True:
    num = int(input("Enter a number between 1 and 3 >> "))
    if(num >= 1 and num <= 3):
        print("Valid entry")
        break


# sleep(3)
system('cls')
people = []
namesCounter = 0
listCounter = 1

names = int(input("How many people do you want to add to the roster? >> "))

while namesCounter < names:
    print("****************************************")
    print(f"Enter person # {listCounter}")
    fname = input("Enter your first name >> ")
    lname = input("Enter your last name >> ")
    age = int(input("What is you age? >> "))
    fullname = fname + " " + lname + " - " + str(age) + " " + "years old"
    people.append(fullname)
    namesCounter += 1
    listCounter += 1

nameListCounter = 1
for person in people:
    print(f'''
    {nameListCounter}.{person}
    ''')
    nameListCounter += 1
print()
