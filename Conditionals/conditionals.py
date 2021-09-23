import os

os.system('cls')

bananas = int(input("How bananas do you have? >> "))
while True:
    if bananas < 0:
        print("What in this world is that number?")
        print("Please try again")
        bananas = int(input("How bananas do you have? >> "))
    else:
       break

if bananas >= 5:
    print(f"I have {bananas} bananas")
elif (bananas >=1 and bananas <=4):
    print(f"I have a small bunch of bananas ({bananas})")
else:
    print("I have no bananas")
