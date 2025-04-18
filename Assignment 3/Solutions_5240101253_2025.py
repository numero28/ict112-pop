"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string = "Programming"

reserved_string = string[::-1]

print(reserved_string)



"""
2.Create a Python program that takes a users full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter Full Name: ")

name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]

formatted_initials = '.'.join(initials) + '.'

print("initials:", formatted_initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string to check for palindrome: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

def count_words_in_sentence():
    sentence = input("Please enter a sentence: ")
    words = sentence.split()
    word_count = len(words)
    print(f"The number of words in the sentence is: {word_count}")

count_words_in_sentence()



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

def replace_is_with_was():
    original_string = "This is a string and it is an example."
    modified_string = original_string.replace("is", "was")
    print("Original String:", original_string)
    print("Modified String:", modified_string)


replace_is_with_was()