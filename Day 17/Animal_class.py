class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "The animal makes a sound."

class Dog(Animal):
    def speak(self):
        return "The dog barks."

dog = Dog("Buddy")
print(dog.name)
print(dog.speak())  