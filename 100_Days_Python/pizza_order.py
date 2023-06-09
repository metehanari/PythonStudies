print("Welcome!")

bill=0

size = input("Select your pizza size: S, M, L\n")

add_pepperoni = input("Do you want pepperoni? Y or N\n")

extra_cheese = input("Do you want extra cheese? Y or N\n")

if size == 'S':
    bill+=15
elif size == 'M':
    bill+=20
elif size == 'L':
    bill+=25


if add_pepperoni== 'Y' and size == 'S' or size=='M':
    bill+=2
if add_pepperoni=='Y' and size=='L':
    bill+=3
if extra_cheese=='Y':
    bill+=1

print(f"Your total bill is {bill}$")