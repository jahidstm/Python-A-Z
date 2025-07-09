import random

choices = ["rock", "paper", "scissor"]

while True:
    computer = random.choice(choices)

    a = input("Enter (rock, paper or scissor) or exit: ")

    if(a == "exit"):
        print("Thanks for playing.")
        break

    if(a not in choices):
        print("Invalid input. Try again!")

    else:
        print(f"Computer choice: {computer}")
        if(a == computer):
            print("It's a tie.")
        elif((a == "rock" and computer == "scissor") or (a == "paper" and computer == "rock") or (a == "scissor" and computer == "paper")):
            print("You win.")
        else:
            print("You lose.")