import re
import utillity

INVALID_CHARACTERS = ['!', '@', '#', '$', '^', '&', '<', '>','=']
CALCULATOR_OPERATIONS = ('*', "**", "+", ")", "(", "/", "-", "%")
EXCEPTION_OPERATIONS = ')'
NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
def check_power(listed_equation):
    while "*" in listed_equation:
        for i in range(len(listed_equation) - 1):
            if i < len(listed_equation) - 1:
                if listed_equation[i] == '*':
                    if listed_equation[i] == listed_equation[i+1]:
                        power = "**"
                        listed_equation[i : i+2] = [power]
        break
def validate_listed_equation(listed_equation): #I: listed equation O: True/False (Valid/Invalid)
    for i in listed_equation:
        if i not in CALCULATOR_OPERATIONS:
            num_index = listed_equation.index(i)
            listed_equation[num_index] = float(i)


    if '(' in listed_equation:
        while '(' in listed_equation:
            for i in range(len(listed_equation)):
                if listed_equation[i] == '(':
                    if listed_equation[i-1] not in CALCULATOR_OPERATIONS:
                        listed_equation.insert(i, '*')
            break

    if '-' in listed_equation:
        i = listed_equation.index('-')
        if ((listed_equation[i-1] in CALCULATOR_OPERATIONS) and (listed_equation[i-1] not in EXCEPTION_OPERATIONS)) or (listed_equation[i] == listed_equation[0]):
            num_after_minus = int(listed_equation[i+1])
            result = (-num_after_minus)
            listed_equation[i : i+2] = [result]
    check_power(listed_equation)
    return True
def validate_equation(stringed_equation): #I: stringed equation O:True/False (Valid/Not valid)
    sequenced_operator = re.findall(r"[+\-*/%=&|^<>!](?:\s*[+\-/%=&|^<>!])+", stringed_equation)
    hanging_operator = re.findall(r"[+\-*/%=&|^<>!]\s*$", stringed_equation)
    started_with_operator = re.findall(r"^\s*[*/%&+|^<>!]", stringed_equation)
    if not started_with_operator == []:
        return "started_with_operator"
    if not hanging_operator == []:
        return "hanging_operator"
    elif not sequenced_operator == []:
        return "sequenced_operator"
    elif stringed_equation == "":
        return "blank"
    elif any(invalid_char in stringed_equation for invalid_char in INVALID_CHARACTERS):
        return "invalid_char"
    elif '(' in stringed_equation and not ')' in stringed_equation:
        return "brackets"
    elif ')' in stringed_equation and not '(' in stringed_equation:
        return "brackets"
    elif "()" in stringed_equation:
        return "empty_brackets"
    else:
        return True
def type_of_invalid_equation(type_error):
    if type_error == "brackets":
        utillity.clear_screen()
        print("You cant put in just one bracket.")
        return False
    elif type_error == "invalid_char":
        utillity.clear_screen()
        print("You've put in invalid characters. Read the instructions.")
        return False
    elif type_error == "blank":
        utillity.clear_screen()
        print("You've put in blank. Read the instructions.")
        return False
    elif type_error == "empty_brackets":
        utillity.clear_screen()
        print("You wrote empty brackets.")
        return False
    elif type_error == "sequenced_operator":
        utillity.clear_screen()
        print("You wrote sequenced operators.")
        return False
    elif type_error == "hanging_operator":
        utillity.clear_screen()
        print("You cant finish with an operator.")
        return False
    elif type_error == "started_with_operator":
        utillity.clear_screen()
        print("You cant start with an operator.")
        return False
    return True
