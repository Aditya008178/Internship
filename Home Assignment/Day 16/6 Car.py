# 6.	Car Service Center
# o	Create a class Car:
# 	Attributes:
# 	brand, model, speed, fuel_level.
# 	Methods:
# 	accelerate() – Increases speed.
# 	brake() – Decreases speed.
# 	add_fuel(amount) – Increases fuel_level.
# 	status() – Prints the status of the car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.fuel_level = 100

    def accelerate(self):
            self.speed += 10
            self.fuel_level -= 20


    def brake(self):
        self.speed -= 5

    def add_fuel(self, amount):
        self.fuel_level += amount

    def display_status(self):
        print(f"Brand: {self.brand} {self.model}")
        print(f"Speed: {self.speed}")
        print(f"Fuel Level: {self.fuel_level}")

c = Car("Toyota", "LC Prado")
c.display_status()
c.accelerate()
c.display_status()
c.brake()
c.display_status()
c.add_fuel(20)
# print("\n")
# c.display_status()
# c.accelerate()
# c.display_status()
# c.brake()
# c.display_status()
# c.add_fuel(20)
# print("\n")
# c.display_status()
# c.accelerate()
# c.display_status()
# c.brake()
# c.display_status()
# c.add_fuel(20)

