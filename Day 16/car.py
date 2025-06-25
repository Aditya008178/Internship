# Create a Car Class
# Attributes:
# brand (string), model (string), speed (initially 0).
# Methods:
# accelerate() — Increases speed by 10.
# brake() — Decreases speed by 5.
# display_speed() — Shows the current speed.
# Test it: Create a car object, call accelerate() and brake() a few times, and display the speed

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 100
    

    def brake(self):
        self.speed -= 50

    def display_speed(self):
        print(f"The current speed is {self.speed} km/h.")
        

c = Car("Toyota", "LC parado")
c.accelerate()
c.brake()
c.display_speed()
