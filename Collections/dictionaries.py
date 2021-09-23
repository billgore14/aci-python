import os
from os import system

system('cls')

myDictList = [{
    "name": "Dunieski",
    "age": 45,
    "isStudent": True 
}, 
{
    "name": "Carlos",
    "age": 25,
    "isStudent": False
}]

# print(myDict['name'])
# print(myDict.get('name'))

dictionaryCounter = 1
for dictionary in myDictList:
    print()
    print("----------------------")
    print(f"Dictionary # {dictionaryCounter}:")
    print("----------------------")
    for key in dictionary:
        print(f'{key}: {dictionary[key]}')
    dictionaryCounter += 1
   #print(myDict[key])

# dictionary_name[key]

# for key, value in myDict.items():
#     print(f'{key}: {value}')


listOfCars= ["Toyota", "BMW", "Nissan", "Mercedes", "Kia"]

print()
print()
print(listOfCars[-1])