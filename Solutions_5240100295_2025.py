"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

# Original string
text = "Programming"

# Reverse the string using slicing
reversed_text = text[::-1]

# Print the reversed string
print("Reversed string:", reversed_text)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

# Get user's full name
full_name = input("Enter your full name: ")

# Split the name into words
name_parts = full_name.strip().split()

# Get the first letter of each part and convert to uppercase
initials = [name[0].upper() for name in name_parts]

# Join the initials with dots
formatted_initials = ".".join(initials) + "."

# Print the result
print("Initials:", formatted_initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

# Get input from the user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
cleaned_text = text.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.strip().split()

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
modified_text = text.replace("is", "was")

# Print the modified string
print("Modified string:", modified_text)
