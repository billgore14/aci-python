
# Data Types

import os 
from os import system
system('cls')

integerNum = 4 # integer type with 32 bits => 4 bytes
longNum = 23456789012121314 # long type with 64 bits => 8 bytes
floatNum = 2.54 # float type with 32 bits => 4 bytes
stringSingle = 'My dog is a beautiful one => single quotes' # string class (single quotes)
stringDouble = "My dog is a beautiful one => double quotes" # string class (double quotes)
stringTriple = '''
    
    
    My dog is a beautiful one
    (triple quotes)


'''
stringNum = "56 => still a string"
isTrue = True # a boolean
isStudent = False # another boolean

# ------ print section --------
# {} => placeholder
print("Integer = {}, Single Quotes String => {}".format(integerNum, stringSingle))
print(f"Integer = {integerNum}")
print(f"Long = {longNum}")
print(f"Float = {floatNum}")
print(f"String => Single quotes = {stringSingle}")
print(f"String => Double quotes = {stringDouble}")
print(f"String => Triple quotes = {stringTriple}")
print(f"Boolean 1 = {isTrue}")
print(f"Boolean 2 = {isStudent}")


