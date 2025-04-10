
"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Answer:

original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Answer:

def get_initials(full_name):
    name_parts = full_name.strip().split()
    initials = [part[0].upper() for part in name_parts if part]
    return '.'.join(initials) + '.'
user_input = input("Enter your full name: ")
print(get_initials(user_input))

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Answer:

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Answer:

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Answer:

text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print(modified_text)

"""
