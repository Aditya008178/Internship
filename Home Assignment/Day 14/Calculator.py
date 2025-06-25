# Calculator Class with Static Methods
# Create a Calculator class:
# add(a, b) — Static method
# multiply(a, b) — Static method
# is_even(number) — Static method
# Test it: Call these methods without creating an object, like:
# Calculator.add(5, 3)  # Returns 8


class Calculator:
    @staticmethod
    def add(a,b):
        print("Addition: ",a+b)

    @staticmethod
    def mul(a,b):
        print("Multiplication: ",a*b)

    @staticmethod
    def even(num):
        if num % 2 == 0:
            print("Even number!")
        else:
            print("Odd number!")

a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
num = int(input("Enter a number to check Even or Odd: "))

ca = Calculator()
ca.add(a,b)
ca.mul(a,b)
ca.even(num)
