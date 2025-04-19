"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# String to reverse
text = "Programming"

# Reverse using string slicing
reversed_text = text[::-1]

# Print the result
print("Original string:", text)
print("Reversed string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get user's full name as input
full_name = input("Enter your full name: ")

# Split the full name into separate words
name_parts = full_name.split()

# Extract the first letter of each word, convert to uppercase and join with periods
initials = ""
for part in name_parts:
    if part:  # Check if the part is not empty
        initials += part[0].upper() + "."

# Print the result
print(f"Your initials are: {initials}")


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(text):
    # Remove spaces and convert to lowercase for a more accurate comparison
    text = text.lower().replace(" ", "")
    
    # Compare the string with its reverse
    if text == text[::-1]:
        return True
    else:
        return False

# Get input from the user
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')


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

# Display the result
print(f"Number of words in the sentence: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")

# Print the original and modified strings
print("Original string:", original_string)
print("Modified string:", modified_string)