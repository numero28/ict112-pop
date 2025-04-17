# Assignment 3 - ICT112
# Student:
#   - Okyere Frimpong Edward (5240101023)
# Year: 2025

# Q1 - Reverse the string "Programming"
original = "Programming"
reversed_str = original[::-1]
print("Q1 - Reversed string:", reversed_str)

# Q2 - Print initials in uppercase from full name
full_name = "Okyere Frimpong Edward"
initials = ".".join([name[0].upper() for name in full_name.strip().split()]) + "."
print("Q2 - Initials:", initials)

# Q3 - Check if a word is a palindrome
word = "madam"  # You can change this to test other words
if word.lower() == word[::-1].lower():
    print(f"Q3 - '{word}' is a palindrome.")
else:
    print(f"Q3 - '{word}' is not a palindrome.")

# Q4 - Calculate the sum of even numbers from 1 to 50
even_sum = sum([num for num in range(1, 51) if num % 2 == 0])
print("Q4 - Sum of even numbers from 1 to 50:", even_sum)

# Q5 - Display multiplication table of a given number
number = 5  # Change this to any number you want
print(f"Q5 - Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
