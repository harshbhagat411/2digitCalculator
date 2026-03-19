# 2-digit calculator

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


# Input from user
num1 = int(input("Enter first number (0-99): "))
num2 = int(input("Enter second number (0-99): "))
operator = input("Enter operator (+, -, *, /): ")

# Check if numbers are 2-digit or less
if 0 <= num1 <= 99 and 0 <= num2 <= 99:
    result = calculate(num1, num2, operator)
    print("Result:", result)
else:
    print("Error: Only 2-digit numbers (0–99) are allowed.")