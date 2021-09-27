class Pizza:
    # constructor/initializer
    def __init__(self, pizzaType=None, size=None, toppings=None, price=None, crust=None, sauce=None):
        self.__pizzaType = pizzaType
        self.__size = size
        self.__toppings = toppings
        self.__price = price
        self.__crust = crust
        self.__sauce = sauce 
        
    # setter or mutator
    def set_pizza_type(self, pizzaType):
        self.__pizzaType = pizzaType
    # getter
    def get_pizza_type(self):
        return self.__pizzaType
    


import os 
from os import system 
system('cls')

# create object pizza
pizza = Pizza("Pepperoni")
# create another object pizza
pizza2 = Pizza()
pizza2.set_pizza_type("Hawaiian")
print(pizza.get_pizza_type(), '-', pizza2.get_pizza_type())


# an object is a class