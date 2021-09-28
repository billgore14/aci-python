import os
import sqlOps as sql
from os import system
from user import User

system('cls')

users = []

# read function
def readUserOperation():
    sql.readUserInfo()

# insert function
def insertOperation():
    numberOfEntries = int(input("Enter number of records >> "))
    for entry in range(numberOfEntries):
        print(f'--- User # {entry + 1} ---')
        user = User()
        fname = input("What is your first name? >> ")
        user.set_firstname(fname)
        lname = input("What is your last name? >> ")
        user.set_lastname(lname)
        age = input("What is your age? >> ")
        user.set_age(age)
        phone = input("What is your phone number? >> ")
        user.set_phone(phone)
        users.append(user)
    for user in users:
        sql.insertUserInfo(user.get_firstname(
        ), user.get_lastname(), user.get_age(), user.get_phone())
    readUserOperation()
