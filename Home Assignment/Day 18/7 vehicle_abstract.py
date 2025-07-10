# 7.Create an abstract class Vehicle:
# o	Abstract methods:
# 	start_engine()
# 	stop_engine()
# o	Implement concrete subclasses:
# 	Car
# 	Motorcycle
# o	Test instances for both.


from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
   
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car's engine is started.")

    def stop_engine(self):
        print("Car's engine is stopped.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle's engine is started.")

    def stop_engine(self):
        print("Motorcycle's engine is stopped.")

car = Car()
car.start_engine()
car.stop_engine()

bike = Motorcycle()
bike.start_engine()
bike.stop_engine()

