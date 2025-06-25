# 3.	Instance vs. Class Attribute Demo
# o	Create a class Student:
# 	Class Attribute: school_name = "ABC High School"
# 	Instance Attributes: name, age, marks
# 	Method:
# 	display() – Shows student details and the school name.
# o	Change school_name for one object, and observe the result on other instances.

class Student:
    school_name = "K.K wagh polytechnic college,Nashik."

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"\nStudent Details: \n")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"School Name: {self.school_name}")

s1 = Student("Aditya", 16, 85)
s2 = Student("Piyush", 17, 90)

s1.display()
s2.display()


s1.school_name = "K.K wagh Agriculture college,Nashik."
print("Changing school name: ")
s1.display()
s2.display()
