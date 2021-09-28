class User:
    def __init__(self, firstName=None, lastName=None, age=None, phone=None):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__phone = phone

    # first name
    def set_firstname(self, firstName):
        self.__firstName = firstName

    def get_firstname(self):
        return self.__firstName

    # last name
    def set_lastname(self, lastName):
        self.__lastName = lastName

    def get_lastname(self):
        return self.__lastName

    # age
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    # phone
    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone
