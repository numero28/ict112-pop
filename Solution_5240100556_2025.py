
"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

def reverse_string(s):

    return s[::-1]



original_string = "Programming"

reversed_string = reverse_string(original_string)

print("Reversed String:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

def print_initials(full_name):

    names = full_name.split()

    initials = ".".join(name[0].upper() for name in names)

    return initials + "."



full_name = input("Enter your full name: ")

initials = print_initials(full_name)

print("Initials:", initials)







"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome(s):

    return s == s[::-1]



string = input("Enter a string: ")

if is_palindrome(string):

    print("The string is a palindrome.")

else:

    print("The string is not a palindrome.")





"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

def count_words(sentence):

    return len(sentence.split())



sentence = input("Enter a sentence: ")

word_count = count_words(sentence)

print("Number of words:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
def replace_is_with_was(s):

    return s.replace("is", "was")



original_string = "This is a string and it is an example."

modified_string = replace_is_with_was(original_string)

print("Modified String:", modified_string)

