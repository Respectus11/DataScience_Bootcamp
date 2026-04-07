
#for addition 
def add(x,y):
    return x+y
#for subtraction 
def subtract(x,y):
    return x-y
#for multiplication
def multiply(x,y):
    return x*y
#for division
def devide(x,y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y
def calculator():
    """Simple CLI calculator."""
    print("Select operation: +, -, *, /")
    op = input("Operation: ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
#checking the operation match it is like switch 
    if op == '+':
        print("Result:", add(x, y))
    elif op == '-':
        print("Result:", subtract(x, y))
    elif op == '*':
        print("Result:", multiply(x, y))
    elif op == '/':
        print("Result:", devide(x, y))
# adding default if the user enter other operation or invalid chr
    else:
        print("Invalid operation")

# Run the calculator
calculator()

    