import random
print("🎲  Welcome to the Dice Roll Simulator!")

while True:
    # Roll the dice
    roll = random.randint(1, 6)
    print(f"\n🎲  You rolled a {roll}!")

    # Ask user if they want to roll again
    choice = input("Do you want to roll again? (yes/no): ").strip().lower()

    if choice != "yes":
        print("Thanks for playing!")
        break