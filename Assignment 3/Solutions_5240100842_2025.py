"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text = "Programming"
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get user input
full_name = input("Enter your full name: ").strip()
# Split the name into parts
name_parts = full_name.split()
# Get the initials
initials = [part[0].upper() for part in name_parts]
# Join the initials with a dot
initials_str = '.'.join(initials)
# Print the result
print(f"Initials: {initials_str}")


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]
# Get user input
user_input = input("Enter a string: ").strip()
# Check if the string is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Get user input
sentence = input("Enter a sentence: ").strip()
# Split the sentence into words
words = sentence.split()
# Count the number of words
word_count = len(words)
# Print the result
print(f"The number of words in the sentence is: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."
# Replace "is" with "was"
modified_string = original_string.replace("is", "was")
# Print the modified string
print(f"Modified string: {modified_string}")
