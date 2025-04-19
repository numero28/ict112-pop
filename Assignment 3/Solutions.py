"""
Solutions to assignment 3
"""

"""
QUESTION 1
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)

"""

"""
QUESTION 2
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]
formatted_initials = '.'.join(initials) + '.'
print("Initials:", formatted_initials)

"""

"""
QUESTION 3
user_input = input("Enter a string: ")
cleaned_string = user_input.lower()
reversed_string = cleaned_string[::-1]
if cleaned_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""


"""
QUESTION 4
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)

"""


"""
QUESTION 5
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print("Modified string:", modified_string)

"""
