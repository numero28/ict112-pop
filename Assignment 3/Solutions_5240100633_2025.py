"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
num_str = "Programming"
print(num_str[::-1]


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

full_name = input("Enter your full name: ")
initials = ".".join(initial[0].upper() for initial in full_name.split()) + "."
print(initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def palindrome(string):
    if string == string[::-1]:
        print(f"{string} is a Palindrome")
    else:
        print(f"{string} is not a Palindrome")

palindrome("level")
palindrome("radar")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence = input("Enter sentence to count words: ")
print(len(sentence.split()))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re

string = "This is a string and it is an example."
modified_string = re.sub(r"\bis\b", "was", string)
print(modified_string)
