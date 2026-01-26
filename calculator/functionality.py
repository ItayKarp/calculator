import sys
import utillity
import calc_project_operators
import re
import validity_calculator

def create_listed_equation(stringed_equation): # I: stringed equation O: listed equation
    listed_equation = re.findall(r"\d+\.?\d*|[+\-*()%//]", stringed_equation)
    return listed_equation

def equation_solver(listed_equation): # I: listed equation O: result of equation
    calc_project_operators.inside_brackets(listed_equation)
    if not calc_project_operators.power(listed_equation):
        return True
    while '*' or '/' or '%' in listed_equation:
        multiplication=len(listed_equation)
        division=len(listed_equation)
        modulo=len(listed_equation)
        if '*' in listed_equation:
            multiplication=listed_equation.index('*')
        if '/' in listed_equation:
            division=listed_equation.index('/')
        if '%' in listed_equation:
            modulo=listed_equation.index('%')
        if modulo < division and modulo < multiplication:
            if not calc_project_operators.modulo(listed_equation, modulo):
                return True
        elif division < modulo and division < multiplication:
            if not calc_project_operators.division(listed_equation, division):
                return True
        elif multiplication < division and multiplication < modulo:
            calc_project_operators.multiply(listed_equation, multiplication)
        if '*' and '/' and '%' not in listed_equation:
            break

    calc_project_operators.add(listed_equation)
    calc_project_operators.sub(listed_equation)
    result = listed_equation[0]
    return result

def restart_calculator(): #I: y/n O: True/False
    user_restart_choice = input("Would you like to make a new calculation? if yes type 'y' if no type 'n'\n").lower()
    if user_restart_choice == 'y':
        utillity.clear_screen()
        return "restart"
    else:
        utillity.exit_cal()
        sys.exit()

def main_calc(stringed_equation, restarted): #I: stringed equation O: Result/Divis
    """

    :param restarted:
    :param stringed_equation:
    :return: result/ DivisionByZero / operator*2
    """
    if restarted == "yes":
        utillity.instructions()
        stringed_equation = input("")
    listed_equation = create_listed_equation(stringed_equation) # I: stringed equation O: listed equation
    validity_calculator.validate_listed_equation(listed_equation) #: not valid listed equation O: valid listed equation
    result = equation_solver(listed_equation)# I: listed equation O: result of equation/False if division by zero
    if equation_solver(listed_equation) == True:
        utillity.clear_screen()
        print("Cant divide by zero.")
        result = main_calc(stringed_equation, "yes")
    print(f"{stringed_equation} = {result}")
    return result
