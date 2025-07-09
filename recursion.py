import random

choices = ['rock', 'paper', 'scissors']
while True:
    computer = random.choice(choices)

    a = input("Enter your choice(rock, paper, scissors) or exit: ")

    if(a == 'exit'):
        print("Thanks for playing! Goodbye!")
        break

    if a not in choices:
        print("Invalid input")

    else:
        print(f"Computer choice: {computer}")
        if computer == a:
            print("It's a tie")

        elif(computer == 'rock' and a == 'scissors') or (computer == 'paper' and a == 'rock') or (computer == 'scissors' and a == 'paper'):
            print("You lose")

        else:
            print("You win")