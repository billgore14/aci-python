import os 
from os import system 
system('cls')

# studentUsernames = []

# for index in range(3):
#    print("******************")
#    print(f"Student # {index + 1}")
#    print("******************")
#    username = input("Username >> ")
#    studentUsernames.append(username)

# for username in studentUsernames:
#     print(username)

# counteri = 0
# counterj = 0
# counterx = 0
# countery = 0

# for i in range(1, 11):  # this will loop 10 times
#     print(' ')
#     print(f'\033[1;31;40mi -----------------{i}')
#     counteri += 1
#     for j in range(1, 6):  # this will loop 5 times
#         print(f'\033[1;33;40mj -----------{j}')
#         counterj += 1
#         for x in range(1, 4):  # this will loop 3 times
#             print(f'\033[1;34;40mx ------ {x}')
#             counterx += 1
#             for y in range(1, 3):  # this will loop 2 times
#                 print(f'\033[1;35;40my - {y}')
#                 countery += 1

# totalCount = counteri + counterj + counterx + countery
# print(f'''\033[0;36;40m
#    i ................. {counteri}
#    j ................. {counterj}
#    x ................. {counterj}
#    y ................. {countery}
#    total count........ {totalCount} 
# ''')


mostOuter = 0
inner = 0
mostInner = 0

for x in range(3):   # outer
    print(f"\033[0;36;40mMost Outer ---- # {x + 1}")
    mostOuter += 1
    for y in range(5): # inner
        print(f"------ \033[0;33;40mInner -- # {y + 1}")
        inner +=1 
        for z in range(7): # most inner
            print(f"------------- \033[0;32;40mMost Inner  # {z + 1}")
            mostInner += 1

print(f"\033[0mMost Outer ----- {mostOuter}")
print(f"Inner ------ {inner}")
print(f"Most Inner ------ {mostInner}")
