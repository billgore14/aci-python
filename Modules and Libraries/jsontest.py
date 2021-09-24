import json , os, time
from json import load
from colorama import Style, Fore, Back
os.system('cls')

x = ["Dunieski", "Otano", 45, 3.98, 4, True]
print(type(x))
x = json.dumps(x) # serialize
print(type(x))
print(x)
x = json.loads(x) # deserialize
print(type(x))
print(x)

print()
print()

time.sleep(3)
os.system('cls')
print("***** Using JSON *****")
print()

try:
    with open('./users.json', 'r') as file:
        datastore = load(file)
        for dictionary in datastore:
            print(Fore.BLUE, f'''
            Name:.................. {dictionary['name']}
            Age:................... {dictionary['age']}
            Educational Level:..... {dictionary['Educational_Level']}
            SSN:................... {dictionary['SSN']}
            ''')
except FileNotFoundError:
    print("File does not exist")


print(Style.RESET_ALL, "I am here")
    


        
