import utillity
import functionality
import validity_calculator
def main():
    user_start = (utillity.menu_cal()).lower()

    if user_start == '2' or user_start == 'exit':
        utillity.exit_cal()
        return False
    elif user_start == '3' or user_start == 'help':
        utillity.help_menu()
        return True
    elif user_start == '1' or user_start == 'start':
        utillity.instructions() # O: instructions
        exercise = input("")
        if not validity_calculator.type_of_invalid_equation(validity_calculator.validate_equation(exercise)): # I: stringed_equation O: True/False = Valid/Invalid
            return True

        result = (functionality.main_calc(exercise, None)) #I: stringed_equation O: result/DivisionByZero/operator*2

        if result == "DivisionByZero":
            utillity.clear_screen()
            print(exercise)
            print("Cant divide by zero.")
        if functionality.restart_calculator(): #O: True/False
            if functionality.main_calc(exercise, "yes") == "DivisionByZero":
                utillity.clear_screen()
                print("You cant divide by zero.")
            functionality.restart_calculator()
            return False
        else:
            return False
    else:
        utillity.clear_screen()
        print("Invalid input. Please enter '1' or 'start' or 'help'")
        main()
        return None


while main():
    main()
