#Ask age and tell how many days,weeks,months left
#until 90 years old.

age = input("What is your age?\n")

remain_years = 90 - int(age)

remain_months = 12 * remain_years 

remain_weeks = 52 * remain_years

remain_days = 365 * remain_years

print(f"You have {remain_days} days, {remain_weeks} weeks and {remain_months} months left.")