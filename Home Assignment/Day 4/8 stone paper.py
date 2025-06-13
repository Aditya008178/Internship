# 8.Rock-Paper-Scissors game (two players):
# o	Take input from both players
# o	Compare:
# 	Rock beats Scissors
# 	Scissors beats Paper
# 	Paper beats Rock
# 	Same → Tie

A = input("Enter input for A (Rock,Paper,Scissors) : ")
B = input("Enter input for B (Rock,Paper,Scissors) : ")


if A == B:
    print("It's a tie!")
elif A == "rock":
    if B == "scissors":
        print("A wins!")
    elif B == "paper":
        print("B wins!")
    
elif A == "paper":
    if B == "rock":
        print("A wins!")
    elif B == "scissors":
        print("B wins!")
    
elif A == "scissors":
    if B == "paper":
        print("A wins!")
    elif B == "rock":
        print("B wins!")

