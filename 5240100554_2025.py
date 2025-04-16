"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Blood"
reversed_string = ""
for rev in original_string:
    reversed_string = rev + reversed_string
print(reversed_string)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    name_parts = full_name.split()
    initials = [name[0].upper() for name in name_parts]
    return ' '.join(initials)
user_full_name = input("Enter your full name: ")
initials = get_initials(user_full_name)
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    return s == ''.join(reversed(s))
string = "radar"
print(is_palindrome(string))




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Please enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The number of words in the sentence is: {word_count}")




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example"
modified_string = original_string.replace(" is", " was")
print(modified_string)
