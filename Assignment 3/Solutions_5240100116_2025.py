"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Given string
string = "Programming"

# Reverse the string using slicing
reversed_string = string[::-1]

# Print the reversed string
print(reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Take full name as input
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.split()

# Initialize an empty string for the initials
initials = ""

# Loop through each part of the name and get the uppercase initial
for part in name_parts:
    initials += part[0].upper() + "."

# Print the initials
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Take input from the user
string = input("Enter a string: ")

# Remove any spaces and convert to lowercase for a case-insensitive check
string = string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words using the split() method
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the number of words
print(f"The number of words in the sentence is: {word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
sentence = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_sentence = sentence.replace("is", "was")

# Print the modified string
print("Modified sentence:", modified_sentence)
