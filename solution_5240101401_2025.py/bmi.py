#Simple BMI calculator
weight = float(input("Enter weight(kg): "))
height = float(input("Enter height(m): "))

bmi = weight / (height * height)

print(f"The bmi is:{bmi:.2f}")

if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Over weight")
elif bmi >= 18:
    print("Normal weight")
else:
    print("Under weight")