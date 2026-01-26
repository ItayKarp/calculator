import os
def clear_screen():
    os.system('clear')
def main_menu():
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
def power(lst):
    print(lst)
    while '**' in lst:
        i = lst.index('**')
        result = lst[i - 1] ** lst[i + 1]
        print(f"{lst[i - 1]} ** {lst[i + 1]} = {result}")
        lst[i] = result
        lst.remove(lst[i - 1])
        lst.remove(lst[i])
def multiply_division(lst):
    i = 0
    print(lst)
    while i < len(lst):
        if lst[i] == '*':
            i = lst.index('*')
            result = lst[i - 1] * lst[i + 1]
            print(f"{lst[i - 1]} * {lst[i + 1]} = {result}")
            lst[i - 1: i + 2] = [result]
        elif lst[i] == '/':
            i = lst.index("/")
            result = lst[i - 1] / lst[i + 1]
            print(f"{lst[i - 1]} / {lst[i + 1]} = {result}")
            lst[i - 1: i + 2] = [result]
        else:
            i += 1

def modulo(lst):
    print(lst)
    while '%' in lst:
        i = lst.index('%')
        result = lst[i - 1] % lst[i + 1]
        print(f"{lst[i - 1]} % {lst[i + 1]} = {result}")
        lst[i-1 : i+2] = [result]
def add_sub(lst):
    print(lst)
    while '+' in lst:
        i = 0
        while i < len(lst):
            if lst[i] == '+':
                res = lst[i - 1] + lst[i + 1]
                print(f"{lst[i - 1]} + {lst[i + 1]} = {res}")
                lst[i - 1: i + 2] = [res]
                i = 0  # Restart scan
            elif lst[i] == '-':
                res = lst[i - 1] - lst[i + 1]
                print(f"{lst[i - 1]} - {lst[i + 1]} = {res}")
                lst[i - 1: i + 2] = [res]
                i = 0  # Restart scan
            else:
                i += 1
def inside_brackets(lst):
    print(lst)
    # Keep processing until no more parentheses
    while '(' in lst:
        # Find the LAST opening parenthesis (innermost one)
        # This handles nested parentheses like ((2+3)*4)
        open_index = -1
        for i in range(len(lst)):
            if lst[i] == '(':
                open_index = i

        # Find the matching closing parenthesis
        close_index = -1
        for i in range(open_index, len(lst)):
            if lst[i] == ')':
                close_index = i
                break

        # Extract what's inside the parentheses
        inside = lst[open_index + 1:close_index]

        # Calculate what's inside (using your existing functions)
        while '**' in inside:
            power(inside)
        while '*' in inside or '/' in inside:
            multiply_division(inside)
        while '+' in inside or '-' in inside:
            add_sub(inside)



        # The result should be a single number now
        result = inside[0]

        # Replace the entire parentheses section with the result
        lst[open_index:close_index + 1] = [result]

    return lst
brackets = []
def main():
    exercise = None
    try:
        user_start = (main_menu())
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    numbers = []
    if user_start == '2' or user_start == 'exit':
        print("Exiting the calculator. Goodbye!")
        return
    elif user_start == '3' or user_start == 'help':
        help_menu()
        main_menu()
        return
    elif user_start == '1' or user_start == 'start':
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
        Example: (3 + 5) * 2 - 4 / 2 ** 2
        Let's get started!\n
        """)
        exercise = input("")
        if exercise == '':
            print("Please enter a valid equation.")
            return

        temp_num = ""
        temp_op = ""
        for i in exercise:
            match i:
                case '1'| '2'| '3'| '4'| '5'| '6'| '7' | '8'| '9'| '0'| '.':
                    if temp_op == "*":
                        numbers.append("*")
                        temp_op = ""
                    temp_num += i
                case '+'| '-'| '/'| '%':
                    if temp_num:
                        numbers.append(float(temp_num))
                        temp_num = ""
                    numbers.append(i)
                    temp_op = ""
                case '*' :
                    if temp_num:
                        numbers.append(float(temp_num))
                        temp_num = ""
                    if temp_op == "*":
                        numbers.append("**")
                        temp_op = ""
                    elif temp_op == "":
                        temp_op = i
                case ' ', '\t', '\n':
                    continue
                case '('| ')':
                    if temp_num:
                        numbers.append(float(temp_num))
                        temp_num = ""
                    if temp_op:  # ← ADD THIS!
                        numbers.append(temp_op)
                        temp_op = ""
                    numbers.append(i)
        if temp_num:
            numbers.append(float(temp_num))
    else:
        print("Invalid input. Please enter a numeric value.")

    inside_brackets(numbers)
    power(numbers)
    multiply_division(numbers)
    modulo(numbers)
    add_sub(numbers)
    result = numbers
    print(f"{exercise} = {result}")
    again = input("Would you like to make a new calculation? if yes type 'y' if no type 'n'").lower()
    if again == 'y':
        clear_screen()
        main()
    else:
        return

main()