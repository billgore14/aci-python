import os
os.system('cls')

# => prints This is simple quotes - "Really?"
print('This is simple quotes - \033[1;32;40m"Really?"')
# => prints Double quotes inside "double" quotes
print("Double quotes inside \033[1;31;40m\"double\" quotes")
# => prints Single quotes inside 'single' quotes
print('Single quotes inside \033[1;33;40m\'single\' quotes')
print("It's is \033[1;34;40mdouble quotes")  # => prints It's is double quotes
print(
    '''This is \033[4;35;40mtriple quotes''')  # => prints This is triple quotes
print()

#  \033[1;35;40m where 35 is the text color and 40 is the background color

name = "\033[0mRobert"
lname = "Clemo"
print(name + " " + lname)  # => Concatenation = append strings => Robert Clemo

# \033[0m => this sets color to normal (regular)


# ***** ASSIGNMENT *****
name1 = "Carlos" # => name1 = Carlos
name2 = name1 # name2 = Carlos
name3 = name2 # name3 = Carlos

name1 = "Pedro"
name4 = "Antonio"
name3 = "Carlos"
name2 = name3 # Carlos
name4 = name2 # Carlos
name1 = name4 # Carlos

apple = "4"
orange = "6"
print(apple + orange) # concatenating 4 + 6 = 46
print(int(apple) + int(orange)) # 4 + 6 = 10

apple = "I am"
orange ="happy"
print(apple + orange)  # returns I amhappy

print()
print("Printing types")
print(f"\033[1;35;40m{type('100')}")
print("\033[0m")
print(f"\033[1;31;40m{type('50')}")
print("\033[0m")
print(f"\033[1;32;40m{type(100)}")
print("\033[0m")
print(f"\033[1;33;40m{type(True)}")
print("\033[0m")
print(f"\033[1;34;40m{type(4.5)}")
print("\033[0m")

name_of_car = "BMW"
nameOfCar = "Mercedes" # camel casing
NameOfCar = "Toyya" # pascal casing, classes

