"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string_to_reverse = "Programming"
reversed_string = string_to_reverse[::-1]
print("Reversed String:", reversed_string)
"""


2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ").strip()
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)
"""


3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string_to_check = input("Enter a string to check if it's a palindrome: ").strip()
is_palindrome = string_to_check == string_to_check[::-1]
print(f"Is the string '{string_to_check}' a palindrome? {is_palindrome}")
"""


4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ").strip()
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)
"""


5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
given_string = "This is a string and it is an example."
modified_string = given_string.replace("is", "was")
print("Modified String:", modified_string)
"""
