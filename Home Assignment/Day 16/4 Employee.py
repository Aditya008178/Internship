# 4.	Employee Salary Manager
# o	Create an Employee class:
# 	Attributes:
# 	Instance: name, salary.
# 	Class Attribute: min_wage = 10000.
# 	Method:
# 	adjust_salary() – If salary < min_wage, set it to min_wage.
# 	display() – Shows employee name and salary.
# o	Test with different employee instances.


class Employee:
    min_wage = 10000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def adjust_salary(self):
        if self.salary<Employee.min_wage:
            self.salary = Employee.min_wage
            print(f"Salary for {self.name} adjusted to minimum wage: {Employee.min_wage}")
        else:
            print(f"Salary for {self.name} is already above minimum wage.")

    def display(self):
        print(f"\nEmployee Details: \n")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


e1 = Employee("Aditya", 8000)
e2 = Employee("Piyush", 15000)


e1.display()
e2.display()


e1.adjust_salary()
e2.adjust_salary()

print("\nAdjust salaries:")
e1.display()
e2.display()


Employee.min_wage = 12000


print("\nChanging wage:")
e1.adjust_salary()
e2.adjust_salary()


e1.display()
e2.display()
