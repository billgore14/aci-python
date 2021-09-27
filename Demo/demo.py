import os, subprocess
from os import system
system('cls')

string = str(input("Enter three words separated by a space  >> "))
print(type(string))
result = string.split(" ")
print(type(result))
print(len(result))

for element in result:
    print(element.lower())
    
    
system("python --version")
subprocess.run(["python", "--version"])
system("dir | findstr Functions")

