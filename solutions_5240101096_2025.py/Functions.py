#Functions
"""
A function to add two numbers
"""
#defining the function
def add_numbers(a, b):
    return a + b

#Calling the function
number1 = 3
number2 = 5
result = add_numbers(number1, number2)
print(f"Sum: {result}")


"""
A function to compute the bmi of a person
"""

#defining the function
def bmi(weight, height):
    return weight / height ** 2

#Calling the function
weight = 90
height = 1.69
result = bmi(weight, height)
print(f"BMI: {result}")
        
"""
A function to compute area of a circle
"""

#defining the function
def area(radius):
    PI = 3.14159
    return radius ** 2 * PI

#Calling the function
radius = 1.69
result = area(radius)
print(f"Area: {result:.2f}")
