# Task: Property Decorators
# Instructions:
# Create a class Student.
# Private attribute: __name.
# Use @property for getting the name.
# Use @name.setter for setting the name, ensuring it’s not an empty string.
# Try creating instances and setting names.

class Student:
    def __init__(self):
        self.__name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            print("Inavalid name")

s = Student()
s.name = "Aditya"
print(s.name)
s.name = ""