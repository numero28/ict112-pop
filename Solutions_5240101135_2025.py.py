"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
text = "Programming"

# Initialize an empty string for the reversed version
reversed_text = ""

# Loop through the original string in reverse order
for char in text:
    reversed_text = char + reversed_text

# Print the reversed string
print("Reversed string:", reversed_text)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Take full name input from the user
full_name = input("Enter your full name: ")

# Split the name into parts (first name, last name, etc.)
name_parts = full_name.strip().split()

# Extract the first letter of each part and convert to uppercase
initials = [part[0].upper() for part in name_parts]

# Join initials with dots and add a trailing dot
formatted_initials = ".".join(initials) + "."

# Print the result
print("Initials:", formatted_initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Take input from the user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for a fair comparison
cleaned_text = text.replace(" ", "").lower()

# Reverse the string
reversed_text = cleaned_text[::-1]

# Check if the original (cleaned) and reversed strings are the same
if cleaned_text == reversed_text:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Use split() to break the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display the result
print("Number of words in the sentence:", word_count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
text = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
# Use " is " with spaces if you want to avoid replacing parts of words like "This"
modified_text = text.replace("is", "was")

# Print the modified string
print("Modified string:", modified_text)
