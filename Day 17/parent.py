# Task:
# Create a parent class Number.

# Create SumNumber and ProductNumber classes that inherit from Number.

# Create a final class FinalCalculator that inherits from both.

# Call parent methods directly:

# SumNumber.sum(self, a, b).

# ProductNumber.product(self, a, b).

# Test:

# FinalCalculator().sum(5, 10) → 15

# FinalCalculator().product(3, 4) → 12
class Number:
    def __init__(self):
        pass

class Sum(Number):
    def sum(self, a, b):
        return a + b

class Product(Number):
    def product(self, a, b):
        return a * b

class FinalCalculator(Sum, Product):
    def __init__(self):
        pass

c= FinalCalculator()
print(c.sum(5, 10))  
print(c.product(3, 4))  