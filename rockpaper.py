import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice: (rock, paper, scissors): ").lower()

if player == computer:
    print("Its a tie.")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

else:
    print(f"You lose! {computer} beats {player}")

