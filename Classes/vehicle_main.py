
import os
from vehicle import Car
from colorama import Style, Back, Fore
os.system('cls')


cars = []


def print_objects(c):
    car_counter = 1
    print()
    print("This is your purchase info:")
    for car in c:
        print(Fore.CYAN, f'''
            Car # {car_counter}
                Make:........ {car.get_make()}
                Model:........ {car.get_model()}
                Year:........ {car.get_year()}
                Color:........ {car.get_color()}
                Price:........ ${car.get_price()}
                Trim:........ {car.get_trim()}
            ''')
        car_counter += 1
    print(Style.RESET_ALL)
    

numberOfCars = int(input("Enter how many cars you purchase >> "))

print("You have chosen to enter", numberOfCars, "cars")
for index in range(numberOfCars):
  print()
  print("********************")
  print("***** CAR #", index + 1, "*****")
  print("********************")
  make = input("What is the make >> ")
  #car.set_make(make)
  model = input("What is the model >> ")
  #car.set_model(model)
  year = input("What is the year >> ")
  #car.set_year(year)
  color = input("What is the color >> ")
  #car.set_color(color)
  price = float(input("What is the price >> "))
  #car.set_price(price)
  trim = input("What is the trim >> ")
  #car.set_trim(trim)
  car = Car(make, model, year, color, price, trim)
  cars.append(car)
  
print_objects(cars)

