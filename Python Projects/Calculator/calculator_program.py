# Python Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return pow(a, b)

# Main Program

while True:
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))

    operator = input("""
    ====== Input an operator ======
            1. +
            2. -
            3. *
            4. /
            5. **
            6. exit
                     
            Input: """)

    try:
        if operator == "1" or operator == "+":
            result = f"Result: {add(a, b)}"

        elif operator == "2" or operator == "-":
            result = f"Result: {subtract(a, b)}"

        elif operator == "3" or operator == "*":
            result = f"Result: {multiply(a, b)}"

        elif operator == "4" or operator == "/":
            if b == 0:
                result = "Cannot divide by zero!"
            else:
                result = f"Result: {divide(a, b)}"

        elif operator == "5" or operator == "**" or operator == "pow":
            result = f"Result: {power(a, b)}"

        elif operator == "6" or operator == "exit":
            break

        else:
            print("An error occurred.")

        print(f"{result}\n")

    except ValueError:
        print("Please input a validated operator.")