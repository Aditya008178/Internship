# 10.	Create a parent class Shape:
# o	Attribute: name
# o	Method: area() returns Not implemented

# 11.	Create child classes:
# o	Rectangle: Inherit from Shape, implement area().
# o	Circle: Inherit from Shape, implement area() using math.pi.
# o	Triangle: Inherit from Shape, implement area() as 0.5 * base * height.

# 12.	Test instances of Rectangle, Circle, and Triangle.


from math import pi
class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        return "Not Implemented"
    

class Rectangle(Shape):
    def __init__(self, name, height, width):
        super().__init__(name)
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5*self.base*self.height

r = Rectangle("Rectangle", 7.5, 9.3)
c = Circle("Circle", 5.5)
t = Triangle("Triangle", 3.5, 5.0)

print("Area of Rectangle: ", r.area())
print("Area of Circle: ", c.area())
print("Area of Triangle: ", t.area())