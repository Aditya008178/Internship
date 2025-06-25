# Create a Rectangle Class
# Attributes: length, width.
# Methods:
# area() — Returns the area of the rectangle.
# perimeter() — Returns the perimeter.
# Test it: Create a few instances and print their area and perimeter

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
            a = self.length * self.width
            print("Area of rectangkle: ",a)

    def perimeter(self):
            p = 2*(self.length + self.width)
            print("perimeter of rectangle: ",p)

l = float(input("Enter length of Rectangle: "))
w = float(input("Enter width of Rectangle:"))

Rect = Rectangle(l,w)
Rect.perimeter()
Rect.area()
