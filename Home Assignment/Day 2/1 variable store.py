# 1.	Create variables to store:
# 	Your name
# 	Your age
# 	Your height in centimeters
# 	A boolean indicating whether you are a student
# Then print all values.

name = input("Enter your name: ")
age = int(input("Enter your age"))
height = float(input("Enter your height"))
student = input("Are you a student? (yes/no): ")

if student== "yes":
    print(f"Name: {name}")
    print(f"age:  {age}")
    print(f"Height: {height}")
