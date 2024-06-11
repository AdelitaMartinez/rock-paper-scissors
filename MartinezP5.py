# MartinezP5
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: provides user capability to play rock scissor paper
# Python version: 3.12.3

import random 

# Welcome message
print("\nWelcome! This program is a rock paper scissors game!")

# Initialize empty list for storing results
game_results = []

# Define choices and victors
choices = ('rock', 'paper', 'scissors')
victor = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

# Determine the winner 
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif victor[user_choice] == computer_choice:
        return "user"
    else: 
        return "computer"

# Initialize game details
rounds = 0
user_wins = 0
computer_wins = 0
ties = 0
play_game = True

# Loop
while play_game: 
    # Get user input, .lower() to avoid errors
    user_choice = input("\nEnter your move (Rock, Paper, Scissors, quit to exit game):  ").lower()
    # If choice is quit, break game
    if user_choice == 'quit':
        break
    # if choice is invalid, try again
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue
    else: 
        # Randomize computer choice using library
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        # If it is a tie, add a point to tie and add result
        if winner == "tie":
            ties += 1
            result = "It's a tie!"
        # Else If user wins, add point to user wins and add result
        elif winner == "user":
            user_wins += 1
            result = "You win!"
        # Else computer wins, add point to computer wins and add result
        else:
            computer_wins += 1
            result = "Computer wins!"

        rounds += 1
        game_results.append({
            "round": rounds,
            "user_choice": user_choice,
            "computer_choice": computer_choice,
            "winner": winner
        })

        # Print results
        print(result)
        print(f"Rounds: {rounds}, User Wins: {user_wins}, Computer Wins: {computer_wins}, Ties: {ties}")

        # Print round summary after every 3 rounds 
        if rounds % 3 == 0:
            print("\nRound Results: ")
            for result in game_results[-3:]:
                print(f"Round {result['round']}: You chose {result['user_choice']}, Computer chose {result['computer_choice']}. Winner is {result['winner']}")

            # Ask user if they would like to play again, .lower() to avoid case errors
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                play_game = False

# Calculate total score 
total_score = user_wins + computer_wins + ties

# Display final results
print("\nGame Over. Here is the final result summary: ")
print(f"Overall Rounds: {total_score}, User Wins: {user_wins}, Computer Wins: {computer_wins}")

# Goodbye and thank you
print("\nThank you for using my program! Goodbye.")
