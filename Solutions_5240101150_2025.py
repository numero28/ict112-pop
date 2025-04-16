"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

def reverse_string(s):
    return s[::-1]

s = "Programming"
print(reverse_string(s))


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def print_initials(full_name):
    names = full_name.split()
    initials = '.'.join(name[0].upper() for name in names)
    return f"{initials}."

full_name = input("Enter your full name: ")
print(print_initials(full_name))



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome(s):
    s = s.lower()  # case-insensitive comparison
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")
print(f"Number of words: {count_words(sentence)}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

def replace_is_with_was(s):
    return s.replace("is", "was")

s = "This is a string and it is an example."
print(replace_is_with_was(s))






