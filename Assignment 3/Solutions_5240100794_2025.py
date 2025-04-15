"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Reverse the string "Programming" using slicing
original_string = "Programming"
reversed_string = original_string[::-1]  # Step -1 reverses the string
print("Reversed string:", reversed_string)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

# Get user input for full name
full_name = input("Enter your full name: ")

# Split the name into parts and extract initials
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]

# Join initials with a '.' and print
formatted_initials = '.'.join(initials) + '.'
print("Initials:", formatted_initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive check
    cleaned = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]

# Input from user
user_input = input("Enter a string to check for palindrome: ")

# Check and print result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")

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

# Display the result
print(f"Number of words in the sentence: {word_count}")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replace 'is' with 'was' (case-sensitive)
modified_string = original_string.replace("is", "was")

# Print the modified string
print("Modified string:", modified_string)
