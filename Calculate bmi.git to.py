weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    classification = "Underweight"
elif 18.5 <= bmi < 25:
    classification = "Normal"
elif 25 <= bmi < 30:
    classification = "Overweight"
else:
    classification = "Obese"

print(f"Your BMI is {bmi:.2f}. You are classified as {classification}.")
