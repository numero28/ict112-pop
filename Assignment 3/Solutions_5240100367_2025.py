"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

def reverse_string():
    original = "Programming"
    reversed_str = original[::-1]
    print(reversed_str)

reverse_string()

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

def print_initials():
    full_name = input("Enter your full name: ")
    parts = full_name.split()
    initials = [part[0].upper() for part in parts]
    print(f"{initials[0]}.{initials[1]}." if len(initials) > 1 else f"{initials[0]}.")

print_initials()

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome():
    word = input("Enter a word: ").lower()
    print("Palindrome!" if word == word[::-1] else "Not a palindrome.")

is_palindrome()

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"Number of words: {len(words)}")

count_words()

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

def replace_is_with_was():
    original = "This is a string and it is an example."
    modified = original.replace(" is ", " was ")
    print(modified)

replace_is_with_was()
