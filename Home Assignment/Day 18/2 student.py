# 2.	Student Class:
# o	Make name and age private.
# o	Use get_name(), set_name() and get_age(), set_age() methods.
# o	Validate age to be a positive integer.

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print("Name: ",self.__name)

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        print("Age: ",self.__age)

    def set_age(self, age):
        if  age > 0:
            self.__age = age
        else:
            print("Age must be a positive integer.")

s =Student("Aditya", 18)
s.set_name("Aditya")
s.set_age(18)
s.get_name()
s.get_age()
