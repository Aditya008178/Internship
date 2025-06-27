# Partially Implemented Abstract Class
# Instructions:
# Create an abstract class named Employee:
# Abstract method: calculate_salary().
# Concrete method: display_role() (prints role).
# Create concrete classes:
# FullTimeEmployee with a calculate_salary() method.
# PartTimeEmployee with a calculate_salary() method.
# Instantiate both and test both methods.

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_role(self, role):
        print(f"{self.name} is a {role}.")

class FullTimeEmployee(Employee):
    def __init__(self, name, a_salary):
        self.name = name
        self.a_salary = a_salary

    def calculate_salary(self):
        print(f"{self.name}'s monthly salary: {self.a_salary / 12}")

class PartTimeEmployee(Employee):
    def __init__(self, name, h_rate, hours):
        self.name = name
        self.h_rate = h_rate
        self.hours = hours

    def calculate_salary(self):
        print(f"{self.name} earned: {self.h_rate * self.hours}")

f_time = FullTimeEmployee("Aditya", 120000)
part_time = PartTimeEmployee("Piyush", 50, 20)

f_time.display_role("Software Engineer")
f_time.calculate_salary()

part_time.display_role("Data Analyst")
part_time.calculate_salary()


    
