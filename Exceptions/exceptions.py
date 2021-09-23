import os 
os.system('cls')

num1 = int(input("Enter a number >> "))
num2 = int(input("Enter another number >> "))
while True:
    if num2 == 0:
        print("Invalid entry")
        num2 = int(input("Enter another number >> "))
    else: 
        break
division = round(num1 / num2, 2)
print(f'''
Division is {division}
''')


print()
print("Oh I am lucky, I have been printed")

try:
    num = int(input("Enter a number >> "))
    print(f"You entered this number {num}")
except ValueError: print(f"Invalid type")


c = 10 # c = 10

c += 11  # c = 21

c -= 11 # c = 10

c *= 3 # c = 30

c /= 15 # c = 2.0

c %= 2 # c = 0
print(c)