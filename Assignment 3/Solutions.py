"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Here's a simple Python program that reverses the string "Programming" using string slicing:

# Original string
text = "Programming"

# Reversing the string using slicing
reversed_text = text[::-1]

# Printing the reversed string
print("Reversed string:", reversed_text)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

Sure! Here's a simple Python program that does exactly that:

# Get user's full name as input
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.strip().split()

# Get the first letter of each part, capitalize it, and add a period
initials = '.'.join([part[0].upper() for part in name_parts]) + '.'

# Print the initials
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Sure! Here's a simple Python program that checks whether a given string is a palindrome:

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

Sure! Here's a simple Python program that counts the number of words in a sentence entered by the user:

def count_words(sentence):
    words = sentence.split()
    return len(words)

# Example usage
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Sure! Here's the Python program to replace all occurrences of "is" with "was" in the given string:

# Original string
text = "This is a string and it is an example."

# Replace all occurrences of 'is' with 'was'
modified_text = text.replace("is", "was")

# Print the modified string
print("Modified string:", modified_text)

