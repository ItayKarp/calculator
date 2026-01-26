import os
import sys
def exit_cal():
    print("Exiting the calculator. Goodbye!")
    sys.exit()
def menu_cal():
    """
    main menu interface
    """
    user_start = input("""
        Welcome to the calculator!
        Main Menu:
        1. Start
        2. Exit
        3. Help for commands
        """).lower()
    return user_start
def help_menu():
    """
    help menu interface
    """
    input("""
                Help Menu:
                - To start the calculator, enter '1' or 'start'.
                - To exit the calculator, enter '2' or 'exit'.
                - operators in the calculator include:
                    + : addition
                    - : subtraction
                    * : multiplication
                    / : division
                    ** : exponentiation
                    % : modulus
                Press Enter to return to the main menu.
                """)
    clear_screen()
    return True
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def instructions():
    print("""Instructions:
            This is an advanced calculator that supports the following operations:
            + : Addition
            - : Subtraction
            * : Multiplication
            / : Division
            ** : Exponentiation
            % : Modulus
            () : Parentheses for grouping
            You can enter complex expressions using these operations.
                    You can't enter any special letters like "!,@,#,$,^,&,<,>".
                    You can't divide by 0.
                    You cannot use square root nor multiply to the power of a negative number.
                    Example: (3 + 5) * 2 - 4 / 2 ** 2
                    Let's get started!\n
                    """)