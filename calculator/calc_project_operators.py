import functionality
def power(listed_equation):
    while '**' in listed_equation:
        i = listed_equation.index('**')
        base = listed_equation[i - 1]
        exponent = listed_equation[i + 1]
        if base == 0 and exponent <0:
            return False
        if 0 < exponent < 1:
            return False
        if exponent < 0:
            return False
        result = base ** exponent
        print(f"{base} ** {exponent} = {result}")
        listed_equation[i-1 : i+2] = [result]
    return True

def multiply(listed_equation, index_operator):
    print(listed_equation)
    result = listed_equation[index_operator - 1] * listed_equation[index_operator + 1]
    print(f"{listed_equation[index_operator - 1]} * {listed_equation[index_operator + 1]} = {result}")
    listed_equation[index_operator-1 : index_operator+2] = [result]

def division(listed_equation, index_operator):
    try:
        i = listed_equation.index('/')
        result = listed_equation[i - 1] / listed_equation[i + 1]
        print(f"{listed_equation[i - 1]} / {listed_equation[i + 1]} = {result}")
        listed_equation[i-1 : i+2] = [result]
        return True
    except ZeroDivisionError:
        print("Cant divide by zero.")
        return False

def modulo(listed_equation, index_operator):
    try:
        result = listed_equation[index_operator - 1] % listed_equation[index_operator + 1]
        print(f"{listed_equation[index_operator - 1]} % {listed_equation[index_operator + 1]} = {result}")
        listed_equation[index_operator-1 : index_operator+2] = [result]
        return True
    except ZeroDivisionError:
        print("Cant divide by zero.")
        return False

def add(listed_equation):
    while '+' in listed_equation:
        i = listed_equation.index('+')
        result = listed_equation[i - 1] + listed_equation[i + 1]
        print(f"{listed_equation[i - 1]} + {listed_equation[i + 1]} = {result}")
        listed_equation[i-1 : i+2] = [result]

def sub(listed_equation):
    while '-' in listed_equation:
        i = listed_equation.index('-')
        result = listed_equation[i - 1] - listed_equation[i + 1]
        print(f"{listed_equation[i - 1]} - {listed_equation[i + 1]} = {result}")
        listed_equation[i-1 : i+2] = [result]

def inside_brackets(listed_equation):
    while '(' in listed_equation:
        open_index = -1
        for i in range(len(listed_equation)):
            if listed_equation[i] == '(':
                open_index = i

        close_index = -1
        for i in range(open_index, len(listed_equation)):
            if listed_equation[i] == ')':
                close_index = i
                break

        inside = listed_equation[open_index + 1:close_index]
        functionality.equation_solver(inside)
        result = inside[0]

        listed_equation[open_index:close_index + 1] = [result]

    return listed_equation