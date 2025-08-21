import re

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



def main():
    user_input = input("Enter an operation ");

    # user_input = user_input.strip().split(" ")
    user_input = re.split(r'\s+|(?=[+\-*/])|(?<=[+\-*/])', user_input.strip())

    result = int(user_input[0])

    for i in range(1, len(user_input), 2):
        operator = user_input[i]
        next_number = int(user_input[i + 1])

        if operator == "+":
            result = addition(result, next_number)
        elif operator == "-":
            result = subtraction(result, next_number)
        elif operator == "*":
            result = multiplication(result, next_number)
        elif operator == "/":
            if next_number == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = division(result, next_number)

    print(f"Result: {result}")
main();
