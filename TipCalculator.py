#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person, should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator.\n")
bill = float(input("What was the total bill? $"))
tip = input("What persentage of tip would you like to give? 10, 12, 15 or Skip? ")

if(tip == "skip"or"Skip"):
    tip = 0
else:
    tip = float(tip)
    
people = int(
    input("Between hoe many poeple would you like to split the bill? "))

payment = (bill / people) * ((100 + tip) / 100)
print(round(payment, 2))