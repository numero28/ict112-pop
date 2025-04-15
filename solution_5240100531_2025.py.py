"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# original strings
text = "programming"

# reversed using slicing
reversed_text = text[::-1]

# print the reversed string
print("reverse_string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# get user's name
full_name = input("Enter your full name: ")

# spilt the name into parts
name_parts = full_name.split()

# get the initials and convert to uppercase
initials = ""
for part in name_parts:
    initials += part[0].upper() + "."

# print the result
print("initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# get input from the user
text = input("Enter a word: ")

# convert to lowercase for case-insensitive comparison
text_lower = text.lower()

# check if the string is equal to its reverse
if text_lower == text_lower[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# slipt the sentence into words
words = sentence.split()

# count the number of words
word_count = len(words)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# original string
text = "This is a string and it is an example."

# replace 'is' with 'was'
modified_text = text.replace("is", "was")

# print the modified string
print("modified_text", modified_text)
