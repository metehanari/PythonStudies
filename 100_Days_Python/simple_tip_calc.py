#bill patterns is like this--> (total/person number) * %tip
#bill must be 2 digits after the point like 12.34

total_bill = float(input("What was the total bill? $"))


tip_percentage = int(input("What percentage to give?"
                        "must be 10, 12 or 15"))

person_number = int(input("How many people to split the bill?"))


personal_pay = (total_bill/ person_number) * (tip_percentage/100 + 1)

personal_pay = "{:.2f}".format((personal_pay))  #a good tip for format manipulation

print(f"Each person should pay: $ {personal_pay}")


