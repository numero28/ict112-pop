"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reversing the string using a loop
reversed_string = ""
for char in original_string:
    reversed_string = char + reversed_string

# Printing the reversed string
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Taking user's full name as input
full_name = input("Enter your full name: ")

# Splitting the name into parts
name_parts = full_name.split()

# Extracting initials and converting them to uppercase
initials = ''.join(part[0].upper() + '.' for part in name_parts)

# Printing the initials
print(initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Taking user input
input_string = input("Enter a string: ")

# Checking if the string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Taking user input for a sentence
sentence = input("Enter a sentence: ")

# Splitting the sentence into words and counting them
word_count = len(sentence.split())

# Printing the number of words
print(f'The number of words in the sentence is: {word_count}')


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""# Original string
original_string = "This is a string and it is an example."

# Replacing "is" with "was"
modified_string = original_string.replace("is", "was")

# Printing the modified string
print(modified_string)
