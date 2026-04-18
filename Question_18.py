# Q18: Accept command-line arguments and perform arithmetic operations

import sys


# Function to perform arithmetic operation
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2

    elif operator == '-':
        return num1 - num2

    elif operator == '*':
        return num1 * num2

    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    else:
        return "Invalid operator"


# ---- Main Execution ----
# sys.argv[0] = filename
# sys.argv[1] = first number
# sys.argv[2] = operator
# sys.argv[3] = second number

if len(sys.argv) != 4:
    print("Usage: python cmd_arithmetic.py <num1> <operator> <num2>")
else:
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    result = calculate(num1, num2, operator)
    print("Result:", result)