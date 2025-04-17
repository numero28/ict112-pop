"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
""Original string
original_string = "Programming"

Reverse the string using slicing
reversed_string = original_string[::-1]

 Print the reversed string
print("Reversed string:", reversed_string)
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""Python program to reverse the string "Programming"

original_string = "Programming"
reversed_string = original_string[::-1]

print("Reversed string:", reversed_string)
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its # Python program to check if a string is a palindrome

def is_palindrome(s):
     Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]

 Input from user
user_input = input("Enter a string: ")

Check and display result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

Split the sentence into words
words = sentence.split()

Count the number of words
word_count = len(words)

Print the word count
print("Number of words in the sentence:", word_count)
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
""" Original string
text = "This is a string and it is an example."

 Replace 'is' with 'was'
modified_text = text.replace("is", "was")

Print the modified string
print(modified_text)
