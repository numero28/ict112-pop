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

# Reversed string using slicing
reversed_text = text[::-1]

# Print the reversed string
print("Reversed string:", reversed_text)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Sure! Here's a simple Python program that does exactly that:

def get_initials(full_name):
    # Split the name into parts (words)
    name_parts = full_name.strip().split()
    
    # Get the first character of each part and capitalize it
    initials = [part[0].upper() for part in name_parts]
    
    # Join with a dot and add a final dot
    return '.'.join(initials) + '.'

# Get user input
user_name = input("Enter your full name: ")
# Print the initials
print("Initials:", get_initials(user_name))




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Here's a simple Python program to check if a given string is a palindrome:

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")

if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Sure! Here's a simple Python program that does exactly that:

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Use split() to break the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display the result
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Here's a simple Python program that replaces all occurrences of "is" with "was" in the given string:

text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print(modified_text)


