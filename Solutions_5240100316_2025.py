"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(user_input_string):
    reversed_string = user_input_string[::-1]
    return reversed_string
user_input_string = "Programming"
reversed_result = reverse_string(user_input_string)
print(reversed_result)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(user_full_name):
    names = user_full_name.split()
    initials = ""

    for name in names:
        initials += name[0].upper() + "."
    return initials[:-1]
user_full_name = input("Enter your full name: ")
initials = get_initials(user_full_name)
print(initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(text):
    processed_text = "".join(c for c in text if c.isalnum()).lower()
    reversed_text = processed_text[::-1]
    return processed_text == reversed_text
user_input_string = input("Enter a string: ")
if is_palindrome(user_input_string):
    print(f"'{user_input_string}' is a palindrome.")
else:
    print(f"'{user_input_string}' is not a palindrome.")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    words = sentence.split()
    return len(words)
user_sentence = input("Enter a sentence: ")
word_count = count_words(user_sentence)
print(f"The sentence has {word_count} words.")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
def replace_is_with_was(input_string):
    modified_string = input_string.replace("is", "was")
    return modified_string
example_string = "This is a string and it is an example."
modified_string = replace_is_with_was(example_string)
print(modified_string)
