from art import Calculator_logo
from replit import clear
print(Calculator_logo)


def cauculator(first_number, next_number, operation):
    result = 0
    if operation == "+":
        result = round(first_number+next_number ,2)
    elif operation == "-":
        result = round(first_number-next_number ,2)
    elif operation == "*":
        result = round(first_number*next_number ,2)
    elif operation == "/" and next_number != 0:
        result = round(first_number/next_number , 2)
    else:
        print("Invalid Input")

    return result
def pick_operation():
    operation_list = ["+", "-", "*", "/"]
    operation = ""
    operation_checker = True
    #Show list of operations
    for i in operation_list:
        print(i)

    while operation_checker:
        operation = str(input("Pick an operation: "))
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            operation_checker = False
        else:
            print("You've entered an invalid operation. Please try again.")
    return operation


def taking_inputs(first_number):    
    operation = pick_operation()

    next_number = float(input("What's the next number?: "))
    result = cauculator(first_number, next_number, operation)
    print(f"{first_number} {operation} {next_number} = {result}")

    continue_calculation = str(input(f"Type 'y' to continue calculating with {cauculator(first_number, next_number, operation)}, or type 'n' to start a new calculation:"))
    return next_number, operation, result, continue_calculation

continue_calculation = "n" #'y' means continue, 'n' means start a new calculation
result = 0
print("Welcome to the Pythonista Calculator!\n") 
while True:
    if continue_calculation == "n":

        first_number = float(input("What's thew first number?: "))  
        calculation_data = taking_inputs(first_number)  #returns next_number, operation, result, and continue_calculation in a list
        result = calculation_data[2]
        continue_calculation = calculation_data[3]
        if continue_calculation == 'n' :
            clear()
            print(Calculator_logo)
    elif continue_calculation == 'y':
        first_number = result
        calculation_data = taking_inputs(first_number)
        result = calculation_data[2]
        continue_calculation = calculation_data[3]
        if continue_calculation == 'n' :
            clear()
            print(Calculator_logo)
    else:
        print("Invalid Input")
        exit()