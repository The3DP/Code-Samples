import time
import os
from enum import Enum


class UserChoice(Enum):
    """Enum for user choices to improve code readability."""
    EXIT = 1
    CONTINUE = 0


def get_user_choice() -> int:
    """
    Prompt user for input and return a valid choice (0 or 1).
    
    Returns:
        int: 0 to continue or 1 to exit
    """
    while True:
        user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ").strip()
        
        if user_input not in ('0', '1'):
            print("Error: Invalid input. Please enter only 0 or 1.")
            continue
        
        return int(user_input)


def exit_program():
    """
    Manage user interaction for exiting or continuing the program.
    """
    print("Welcome to the program!")
    print("This program allows you to either continue or exit.")
    print("Enter '1' to exit or '0' to continue.")
    
    choice = get_user_choice()
    
    if choice == UserChoice.EXIT.value:
        _handle_exit()
    else:
        _handle_continue()
    
    # Log the action
    log_action(choice)


def _handle_exit():
    """Handle exit logic."""
    print("\nYou have chosen to exit the program. Goodbye!")
    print("Exiting the program... Saving progress and shutting down.")
    time.sleep(2)  # Simulate saving progress
    # Add cleanup code here if needed (close files, save data, etc.)


def _handle_continue():
    """Handle continue logic."""
    print("\nYou have chosen to continue. The program will continue running.")
    perform_task()


def perform_task():
    """
    Execute the next task in the program.
    """
    print("Performing the next task...")
    # Add your task logic here


def log_action(choice: int) -> None:
    """
    Log user action for debugging/tracking purposes.
    
    Args:
        choice: The user's choice (0 or 1)
    """
    action = "exit" if choice == UserChoice.EXIT.value else "continue"
    # Implement logging (file, database, etc.)
    # Example: logger.info(f"User chose to {action}")
    pass
