# Creating a rock,paper,scissors game.

from random import randint
moves = ("rock", "paper", "scissors")
while True:
    computer = moves[randint(0,2)]
    player = input("Rock, Paper, Scissors? (or end) ").lower().strip()
    if player == "end":
        break
    elif player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose! I chose paper!")
        else:
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("You lose! I chose scissors!")
        else:
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("You lose! I chose rock!")
        else:
             print("You win!")
    else:
        print("Check your spelling!")
