import random


# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"


# Main program
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your Score: {user_score}, Computer Score: {computer_score}")

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print('okay')
        break
    else:
        print('sure')

print("Thank you for playing!")
