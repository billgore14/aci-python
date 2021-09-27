class Car:
    def __init__(self, make=None, model=None, year=None, color=None, price= None, trim=None):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__trim = trim
        
    def set_make(self, make): # setter or mutator
        self.__make = make
    def get_make(self): # getter
        return self.__make
    
    def set_model(self, model):  # setter or mutator
        self.__model = model
    def get_model(self):  # getter
        return self.__model
    
    def set_year(self, year):  # setter or mutator
        self.__year = year
    def get_year(self):  # getter
        return self.__year
    
    def set_color(self, color):  # setter or mutator
        self.__color = color
    def get_color(self):  # getter
        return self.__color
    
    def set_price(self, price):  # setter or mutator
        self.__price = price
    def get_price(self):  # getter
        return self.__price

    def set_trim(self, trim):  # setter or mutator
        self.__trim = trim
    def get_trim(self):  # getter
        return self.__trim
   

    
        




