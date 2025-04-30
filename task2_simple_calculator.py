'''
Task 2: Simple Calculator

Write a small program that:

Asks the user for:

    First number

    Operator (+, -, *, /)

    Second number

Performs the operation and prints the result.

'''

def simple_calculator():
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")
        return

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = first_number / second_number
    else:
        print("Invalid operator. Please use one of the following: +, -, *, /")
        return
    
    print(f"The result of {first_number} {operator} {second_number} is: {result}")


simple_calculator()