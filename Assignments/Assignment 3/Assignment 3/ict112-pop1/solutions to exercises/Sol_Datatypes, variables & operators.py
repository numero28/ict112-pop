#Exercise 1
print("""
Hello, World!
Welcome to Python programming
""")

#Exercise 2
print("""
STARRY TRIANGLE
===============
""")

print("*")
print("**")
print("***")
print("****")
print("*****")

#Exercise 3
print("Hello, World! Welcome to Python programming")

#Exercise 4
print("""
ALICE'S BIO
=========
""")

age = 30
name = "Alice"

print(f"Name: {name}")
print("Age:", age)


#Exercise 5
print("""
FRUIT LIST
==========
""")
print("""
Apple
Banana
Cherry
Date""")

#Exercise 6
print("""
PERSONAL BIO DATA
=================
""")

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello {name} ! You are {age} years old")

#Exercise 7
print("""
ADD TWO NUMBERS APP
===================
""")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = number1 + number2

print(f"The sum of {number1} and {number2} is {result}")

#Exercise 8
print("""
FAVOURITE STUFF
===============
""")

color = input("Emter your favourite colour: ")
food = input("Enter your favourite food: ")

print(f"Your favourite colour is {color} and your favourite food is {food}")

#Exercise 9
print("""
CALCULATOR APP
==============
""")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print(f"The sum of {number1} and {number2} is {addition}")
print(f"The difference of {number1} and {number2} is {subtraction}")
print(f"The product of {number1} and {number2} is {multiplication}")
print(f"The quotient of {number1} and {number2} is {division}")

#Exercise 10
print("""
AREA OF A CIRCLE
================
""")

PI = 3.14159
radius = float(input("Enter the radius: "))
area = PI * (radius **2)

print(
f"""
The area of a circle with Radius {radius}
      is {round(area,2)}
""")


#BMI Calculator
print("""
BMI CALCULATOR
==============
""")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

body_mass_index = weight / (height * height)

print(f"Your BMI is: {body_mass_index}")

if body_mass_index >= 30:
    print("You are obese")
elif body_mass_index >= 25:
    print("You are over weight")
elif body_mass_index >= 18.5:
    print("You are or a normal weight")
else:
    print("You are under weight")
