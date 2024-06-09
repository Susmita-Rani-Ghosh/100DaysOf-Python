MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

# function for displaying options
def display():

    UserInput = ""
    while UserInput != "espresso" and UserInput != "latte" and UserInput != "cappuccino" and UserInput != "off" and UserInput != "report":
        UserInput = str(input("What would you like? (espresso/latte/cappuccino).\nFor report type 'report': "))
    if UserInput == "espresso" or UserInput == "latte" or UserInput == "cappuccino":
        price = MENU[UserInput]["cost"]
        print(f"Price: {price}")
    return UserInput

# display price for selected item.

# create functions for calculating money inserted.
def payment():
    quarters = int(input("Insert number of quarters: "))
    dimes = int(input("Insert number of dimes: "))
    nickles = int(input("Insert number of nickles: "))
    pennies = int(input("Insert number of pennies: "))
    payment = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return payment

#function for checking resource efficiency
def resourceEfficiency(item):
    """returns true if where is enough resource available. If then ten returns false"""
    water = MENU[item]["ingredients"]["water"]
    try :
        milk = MENU[item]["ingredients"]["milk"]
    except KeyError:
        milk = 0
    coffee = MENU[item]["ingredients"]["coffee"]
    if resources["water"]>= water and resources["milk"]>= milk and resources["coffee"]>= coffee:
        return True
    else:
        return False

#  function for printing report
def printReport():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")


# function for turning machine off.
#  function for making coffee and updating resource and money amount.
def updateResource(item):

    resources["water"] = resources["water"] - MENU[item]["ingredients"]["water"]
    try:
        resources["milk"] = resources["milk"] - MENU[item]["ingredients"]["milk"]
    except KeyError:
        pass  #continue the code with no changes.
    resources["coffee"] = resources["coffee"] - MENU[item]["ingredients"]["coffee"]


def coffeMachine():
    global money
    CoffeeMachineOn = True
    while CoffeeMachineOn:
        continuemaking = False
        userChoice= display()

        if userChoice == "off":
            CoffeeMachineOn = False
            print("    Turning the Coffee Machine off 👋.")
            continue
        elif userChoice == "report":
            printReport()
            continue
        else:
            beverage = userChoice
            price = MENU[beverage]["cost"]
            resourcEfficinecy = resourceEfficiency(beverage)

        if resourcEfficinecy:
            paid = payment()
        else:
            print("Sorry, there is not enough resource available. ")
            continue

        if paid >= price:
            continuemaking = True
        else:
            continuemaking = False
            print("Sorry, Not enough money. Money refunded.")
            continue

        if continuemaking:
            if (paid > price):
                print(f"Here is ${round(paid-price, 2)} change for you!")


            if resourcEfficinecy:
                money = money + price
                updateResource(beverage)
                print(f"Here is your {beverage} ☕. Enjoy!")


coffeMachine()
