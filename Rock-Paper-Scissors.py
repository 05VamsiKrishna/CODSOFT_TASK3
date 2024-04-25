import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print("Result:", result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Final Scores:")
            print("User:", user_score)
            print("Computer:", computer_score)
            break

play_game()
