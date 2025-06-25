# Create a class Number:

# Attribute: value.

# Create a class SquareNumber that inherits from Number:

# Method: square() → returns value * value.

# Create a class CubeNumber that inherits from SquareNumber:

# Method: cube() → returns value * value * value.

# Test:

# Number(2) → value = 2

# SquareNumber(3).square() → 9

# CubeNumber(3).cube() → 27
class Number:
    def __init__(self, value):
        self.value = value

class Square(Number):
    def square(self):
        return self.value * self.value

class Cube(Square):
    def cube(self):
        return self.value * self.value * self.value

num = Number(2)
print(f"Value:bn{num.value}")

square = Square(3)
print(f"Square of {square.value}:{square.square()}")

cube = Cube(3)
print(f"cube of {cube.value}:{cube.cube()}")
