"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Reverse the string using a loop
original_string = "Programming"
reversed_string = ""

for char in original_string:
    reversed_string = char + reversed_string

# Print the reversed string
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get full name input from the user
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.split()

# Extract and print the initials in uppercase
initials = ".".join([part[0].upper() for part in name_parts])
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check if a string is a palindrome
def is_palindrome(string):
    # Remove spaces and convert to lowercase for consistency
    cleaned_string = string.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Get user input
input_string = input("Enter a string: ")

# Check and print the result
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome!')
else:
    print(f'"{input_string}" is not a palindrome.')




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("The number of words in the sentence is:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")

# Print the modified string
print("Modified string:", modified_string)

