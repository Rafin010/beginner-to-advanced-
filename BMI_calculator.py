'''
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    bmi = weight / ( height ** 2)

    if bmi <=  18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi_value = weight / (height ** 2)
bmi_category = bmi(weight, height)

print(f"BMI: {bmi_value:.2f}")
print(f"Category: {bmi_category}")

 






