#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## import random

# Function to calculate the computer's move
def computer_move(current_total, player_first, first_move=False):
    """
    Calculate the computer's move.
    
    If the player goes first, the computer aims to make the total 12, 23, 34, 45, 56, 67, 78, 89, or 100.
    If the computer goes first, it will always play to keep the total at the form of 11x + 1.
    The move must be between 1 and 10.
    """
    if player_first:
        # Targets for computer when the player goes first
        targets = [12, 23, 34, 45, 56, 67, 78, 89, 100]
        for target in targets:
            if target > current_total:
                move = target - current_total
                if 1 <= move <= 10:
                    return move
        # If no valid move found, play a random valid move between 1 and 10
        return random.randint(1, 10)
    else:
        if first_move:
            return 1
        for move in range(1, 11):
            if (current_total + move) % 11 == 1:
                return move
        return random.randint(1, 10)  # Backup move if no optimal move is found

# Function to get the player's move
def player_move():
    """
    Get the player's move.
    
    The player must choose a number between 1 and 10.
    """
    while True:
        try:
            move = int(input("Your move (choose a number between 1 and 10): "))
            if 1 <= move <= 10:
                return move
            else:
                print("Invalid move. Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")

# Function to get the player's choice
def get_player_choice():
    """
    Get the player's choice whether to play first or second.
    """
    while True:
        choice = input("Do you want to play first or second? (Enter 'first' or 'second'): ").strip().lower()
        if choice in ['first', 'second']:
            return choice
        else:
            print("Invalid input. Please enter 'first' or 'second'.")

# Function to display game rules
def display_rules():
    """
    Display the game rules.
    """
    print("Welcome to The 100 Game!")
    print("Rules:")
    print("1. The game starts with a total of 0.")
    print("2. Players take turns adding a number between 1 and 10 to the total.")
    print("3. The player who makes the total number of exactly 100 wins.")
    print("=" * 30)

# Function to play the game
def play_game():
    """
    Play the 100 game.
    
    The player chooses whether to play first or second.
    """
    display_rules()
    
    player_choice = get_player_choice()
    player_first = (player_choice == 'first')
    
    current_total = 0
    print("Starting the game. Current total: 0")
    print("=" * 30)
    
    move_history = []

    if not player_first:
        # Computer's first move
        comp_move = computer_move(current_total, player_first=False, first_move=True)
        current_total += comp_move
        move_history.append(f"Computer plays: {comp_move}")
        print(f"Computer plays: {comp_move}")
        print(f"Current total: {current_total}")
        print("-" * 30)
    
    while current_total < 100:
        if player_first or current_total != 0:
            # Player's turn
            player_move_value = player_move()
            current_total += player_move_value
            move_history.append(f"You play: {player_move_value}")
            print(f"You play: {player_move_value}")
            print(f"Current total: {current_total}")
            print("-" * 30)
            if current_total >= 100:
                print("You win!")
                break
        
        # Computer's turn
        comp_move = computer_move(current_total, player_first=player_first)
        current_total += comp_move
        move_history.append(f"Computer plays: {comp_move}")
        print(f"Computer plays: {comp_move}")
        print(f"Current total: {current_total}")
        print("-" * 30)
        if current_total >= 100:
            print("Computer wins!")
            break
    
    print("\nMove History:")
    for move in move_history:
        print(move)

# Start the game
play_game()

