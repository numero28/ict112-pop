"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Original string
original_string = "Programming"

# Reversing the string using slicing
reversed_string = original_string[::-1]

# Printing the reversed string
print("Reversed string:", reversed_string)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Input string
input_string = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison (optional)
normalized_string = input_string.lower()

# Check if it's a palindrome
if normalized_string == normalized_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')



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

# Print the word count
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replace all occurrences of 'is' with 'was'
# Using a space before 'is' to avoid changing 'This' to 'Thwas'
modified_string = original_string.replace(" is", " was")

# Print the modified string
print("Modified string:", modified_string)
