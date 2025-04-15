"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reversed string using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Take full name as input from the user
full_name = input("Enter your full name: ")

# Split the name into parts (words)
name_parts = full_name.split()

# Get the first letter of each part and convert to uppercase, then add a dot
initials = ".".join([part[0].upper() for part in name_parts]) + "."

# Print the initials
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Take input from the user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for a fair comparison
clean_text = text.replace(" ", "").lower()

# Check if the cleaned text is the same forwards and backwards
if clean_text == clean_text[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words using split()
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re

# Original string
text = "This is a string and it is an example."

# Replace only full word 'is' with 'was' using regular expressions
modified_text = re.sub(r'\bis\b', 'was', text)

# Print the modified string
print("Modified string:", modified_text)
