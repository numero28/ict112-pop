"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reversing the string using slicing
reversed_string = original_string[::-1]

# Printing the reversed string
print("Reversed string:", reversed_string)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get input from the user
input_string = input("Enter a string: ")

# Convert to lowercase to make the check case-insensitive (optional)
input_string = input_string.lower()

# Check if the string is equal to its reverse
if input_string == input_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Get input from the user
input_string = input("Enter a string: ")

# Convert to lowercase to make the check case-insensitive (optional)
input_string = input_string.lower()

# Check if the string is equal to its reverse
if input_string == input_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Use split() to break the sentence into words
words = sentence.strip().split()

# Count the number of words
word_count = len(words)

# Print the result
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
