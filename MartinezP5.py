# MartinezP5
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: provides user capability to play rock scissor paper
# Python version: 3.12.3

import random 

# Welcome message
print("Welcome! This program is a rock paper scissors game!")

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

# Loop
while True: 
  # Get user input, .lower() to avoid errors
  user_choice = input("\nEnter your move: Rock, Paper, Or scissors (or 'quit' to stop playing): ").lower()
  # If choice is quit, break game
  if user_choice == 'quit':
    break
  # if choice is invalid, try again
  if user_choice not in choices:
    print("invalid choice, please try again.")
    continue

# Display results

# Goodbye and thank you