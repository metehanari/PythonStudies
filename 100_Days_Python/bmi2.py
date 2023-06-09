#bmi calculator with interpretation
height = float(input("enter your height in m : \n"))
weight = float(input("enter your weight in kg : \n"))

bmi = weight/(height**2)

bmi = round(bmi,2) #format manipulation for 2 decimal digits

if bmi<18.5:
    print(f"Your BMI is {bmi} and you are underweight\n")
elif bmi<25:
    print(f"Your BMI is {bmi} and you are normal weight\n")
elif bmi<30:
    print(f"Your BMI is {bmi} and you are overweight\n")
elif bmi<35:
    print(f"Your BMI is {bmi} and you are obese\n")
else:
    print(f"Your BMI is {bmi} and you are clinically obese\n")


