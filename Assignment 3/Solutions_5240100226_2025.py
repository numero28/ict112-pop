"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_str = "Programming"
reversed_str = ""
for char in original_str:
    reversed_str = char + reversed_str
print(reversed_str)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]
formatted_initials = '.'.join(initials) + '.'
print(formatted_initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
def is_palindrome(s):
"""
def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")
# Check and print the result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")


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
print(f"The number of words in the sentence is: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)