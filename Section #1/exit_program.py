import time
import os

def exit_program():
    """
    This function manages the user interaction for exiting or continuing the program.
    The user can input 1 to exit, 0 to continue, or any invalid input to prompt the user for correct input.
    """
    # Initialize variable 'ex' with a value other than 1 or 0 to start the loop
    ex = 2

    print("Welcome to the program!")
    print("This function allows you to either continue or exit the program.")
    print("You can enter '1' to exit the program or '0' to continue the program.")

    # Start a loop that will continue until the user enters either '1' or '0'
    while ex != 1 and ex != 0:
        try:
            # Prompt the user for input
            user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")

            # Check if the input is a digit (i.e., an integer string)
            if user_input.isdigit():
                ex = int(user_input)  # Convert the input string to an integer
            else:
                # If input is not a digit, prompt the user for a valid input
                print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")

            # Display different messages depending on the input
            if ex == 1:
                print("\nYou have chosen to exit the program. Goodbye!")
            elif ex == 0:
                print("\nYou have chosen to continue. The program will continue running.")
            else:
                print("Error: Input out of expected range. Please enter only 1 or 0.")

        except ValueError:
            # If there's any error during input (though unlikely with 'isdigit' check)
            print("Error: Something went wrong while processing your input. Please try again.")

    # Additional behavior after exiting or continuing
    # Here, we simulate a program performing additional actions based on the user's choice
    if ex == 1:
        print("Exiting the program... Saving progress and shutting down.")
        time.sleep(2)  # Simulate the time it might take to save progress
        # You could add code here to save data or clean up resources if needed
    elif ex == 0:
        print("Continuing the program... Performing the next task.")
        # Code for continuing the program goes here
        perform_task()

    # Log action (whether the user exited or continued) for debugging or tracking purposes
    log_action(ex)


def perform_task():
    """
    Simulates performing a task in the program after the user chooses to continue.
