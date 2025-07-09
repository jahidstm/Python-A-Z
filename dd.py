import random

# Define the valid choices
choices = ['rock', 'paper', 'scissors']

while True:
    # Computer makes a random choice
    computer = random.choice(choices)

    # Get user input
    user_choice = input("Enter your choice (rock, paper, scissors) or type 'quit' to exit: ").lower()

    # Check if the user wants to quit
    if user_choice == 'quit':
        print("Thanks for playing! Goodbye!")
        break

    # Check if the user's input is valid
    if user_choice not in choices:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue  # Skip the rest of the loop and prompt the user again

    # Display the computer's choice
    print(f"Computer choice: {computer}")

    # Determine the outcome
    if computer == user_choice:
        print("It's a tie")
    elif (computer == 'rock' and user_choice == 'scissors') or \
         (computer == 'paper' and user_choice == 'rock') or \
         (computer == 'scissors' and user_choice == 'paper'):
        print("You lose")
    else:
        print("You win")

    print()  # Add a blank line for better readability between rounds