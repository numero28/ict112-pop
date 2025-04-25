"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reverse the string using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Take user input
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.split()

# Extract and capitalize the initials
initials = ".".join([part[0].upper() for part in name_parts]) + "."

# Print the initials
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Take input from the user
text = input("Enter a string: ")

# Convert to lowercase to make it case-insensitive
text = text.lower()

# Check if the string is equal to its reverse
if text == text[::-1]:
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
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words:", word_count)



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
