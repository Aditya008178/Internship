# 7.	Employee Class
# Attributes:
# 	Class Attribute: company_name = "TechCorp"
# 	Instance Attributes: name, salary
# Method:
# 	give_raise(percent) – Increases the employee’s salary by the given percentage.
# 	display() – Prints employee details.



class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary *= (1 + percent / 100)
        print(f"Salary increased by {percent}% for {self.name}.")

    def display(self):
        print(f"\nEmployee Details")
        print(f"Name: {self.name}")
        print(f"Company: {Employee.company_name}")
        print(f"Salary: {self.salary:.2f}")

e1 = Employee("Aditya", 50000)
e2 = Employee("Piyush", 60000)

e1.display()
e2.display()

e1.give_raise(10)
e2.give_raise(10)
