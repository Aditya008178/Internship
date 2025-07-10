# Simple Reflex Agent – Vacuum Cleaner
# 🔹Objective:
# Simulate a simple reflex agent for a 1D or 2D vacuum cleaner world.
# 🔹Instructions:
# Create an environment as a list of rooms: e.g. ['Dirty', 'Clean', 'Dirty']
# Agent starts at position 0.
# If the current position is 'Dirty' → clean it.
# Move to the next room and repeat.
# Stop when all rooms are clean.

class Vaccum_cleaner:
    def __init__(self, enviroment):
        self.enviroment = enviroment
        self.position = 0


    def clean(self):
        while "dirty" in self.enviroment:
            if self.enviroment[self.position] == "dirty":
                print("Cleaning Room: ",self.position)
                print(f"Room {self.position} is clean")

    def move_room(self):
        self.position=(self.position+1) % len(self.enviroment)
        print("Move to romm: ", self.position)

enviroment = ["dirty","clean","dirty","dirty","clean"]

vaccum = Vaccum_cleaner(enviroment)
vaccum.clean()


    