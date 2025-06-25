# 14.	Create a shapes.py:
# o	area_of_rectangle(length, breadth).
# o	area_of_circle(radius).
# o	area_of_square(side).
# o	Import and test these in main.py. (main4.py)

def area_of_rectangle(length, breadth):
    area = length*breadth
    print("Area of Rectangle: ", area)

def area_of_circle(radius):
    area = 3.14*radius*radius
    print("Area of Circle: ", area)

def area_of_square(side):
    area = side*side
    print("Area of Square: ", area)