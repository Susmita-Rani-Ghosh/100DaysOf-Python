from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import Auction_logo

print(Auction_logo)
print("Welcome to the Secret Auction\n")

Auction_data = {}
Continue = True

while Continue:
    name = str(input("What is your name?: "))
    amount = int(input("What's your bid?: "))
    Auction_data[name] = amount
    Continue = input(
        "Are there any other bidders? Type 'yes' or 'no': ").lower()
    if Continue == "yes":
        Continue = True
    elif Continue == "no":
        Continue = False
    else:
        print("Invalid Input")
        Continue = False
    clear()


def find_highest_bidder(Auction_data):
    max_bid = 0
    winner = ""
    for key in Auction_data:
        if int(Auction_data[key]) > max_bid:
            max_bid = int(Auction_data[key])
            winner = key
    print(f"The winner is {winner} with a bid of ${max_bid}.")


#function call
find_highest_bidder(Auction_data)
