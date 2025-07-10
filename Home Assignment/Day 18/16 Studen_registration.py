# 16.	Build a robust Student Registration System:
# o	Abstract class: Person
# 	Abstract method: get_role()
# o	Subclasses:
# 	Student (encapsulates marks and validates range).
# 	Teacher (encapsulates salary).
# 	AdminStaff (encapsulates department).

from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def get_role(self):
        pass


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name, "Student")
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks


    def get_marks(self):
        return self.__marks

    def get_role(self):
        return self.role

class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name, "Lecturer")
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return self.role

class AdminStaff(Person):
    def __init__(self, name, department):
        super().__init__(name, "Administrator")
        self.__department = department

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def get_role(self):
        return self.role

student = Student("Piyush", 78)
print(f"Marks of {student.name} : {student.get_marks()}")
student.set_marks(90)
print(f"Updated marks of {student.name} : {student.get_marks()}")

teacher = Teacher("Mr.Prasad", 45000)
teacher.set_salary(50000)
print(f"Salary of {teacher.name} ({teacher.get_role()}) is {teacher.get_salary()}.")

admin_staff = AdminStaff("Mr.Aditya", "Technical Department")
print(f"Department of {admin_staff.name} ({admin_staff.get_role()}) is {admin_staff.get_department()}.")
    