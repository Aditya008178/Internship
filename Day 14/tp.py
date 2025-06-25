#create a game of stone paper scissor 
import random
def play_game():
    choices = ['stone', 'paper', 'scissor']
    user_choice = input("Enter your choice (stone, paper, scissor): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose from stone, paper, or scissor.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")