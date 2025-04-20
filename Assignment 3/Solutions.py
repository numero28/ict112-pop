"""
Solutions to assignment 3
"""

"""
SOLUTION 1
string = "Programming"
reversed_string = string[::-1]
print(reversed_string)

"""



"""
SOLUTION 2
def get_initials(name):
 name_parts = name.split()
 initials = ".".join([part[0].upper() for part in name_parts])
 return initials + "."
full_name = input("Enter your full name: ")
print(get_initials(full_name))

"""



"""
SOLUTION 3
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""



"""
SOLUTION 4
def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: "
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")

"""



"""
SOLUTION 5
input_string = "This is a string and it is an example."
modified_string = input_string.replace(" is ", " was ")
print(modified_string)

"""
