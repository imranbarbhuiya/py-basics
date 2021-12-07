print("Welcome to BMI Calculator")

height = int(input("What is your Height in m\n"))
weight = int(input("What is your Weight in kg\n"))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI Score is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Your BMI Score is {bmi}, You are normal Weight")
elif bmi < 30:
    print(f"Your BMI Score is {bmi}, You are overWeight")
elif bmi < 35:
    print(f"Your BMI Score is {bmi}, You are obese")
else:
    print(f"Your BMI Score is {bmi}, You are clinically obese")
