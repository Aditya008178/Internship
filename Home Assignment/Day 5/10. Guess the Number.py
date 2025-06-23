# 11.	Guess the Number Game
# •	Set a secret number (e.g., 7)
# •	Let the user guess until they get it right
# •	Print "Too high" or "Too low" for wrong guesses
# •	Print "Correct!" when guessed

s_num = 9

while True:

    guess = int(input("Guess the number: "))
    if s_num > guess:
        print("Too low")
    elif s_num < guess:
        print("Too high")
    else:
        print("Correct")
        