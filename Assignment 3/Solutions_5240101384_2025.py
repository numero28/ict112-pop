#QUESTION 1
"""
# Original string
original_string = "Programming"

# Reversing using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print(reversed_string)
"""
#QUESTION 2
"""
# Take full name input from user
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.strip().split()

# Get the initials and capitalize them
initials = ".".join([part[0].upper() for part in name_parts]) + "."

# Print the initials
print("Initials:", initials)
"""
#QUESTION 3
"""
# Take input from the user
input_string = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison (optional)
normalized_string = input_string.lower()

# Check if the string is equal to its reverse
if normalized_string == normalized_string[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

"""
#QUESTION 4
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the word count
print("Number of words in the sentence:", word_count)
"""
#QUESTION 5
import re

original_string = "This is a string and it is an example."

modified_string = re.sub(r'\bis\b', 'was', original_string)

print("Modified string:", modified_string)



