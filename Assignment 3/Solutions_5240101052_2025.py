"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    initials = ''.join([name[0].upper() + '.' for name in full_name.split()])
    return initials

user_input = input("Enter your full name: ")
print(get_initials(user_input))



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Palindrome Checker

def is_palindrome(s):
    return s == s[::-1]

# Example usage
string_to_check = "radar"
if is_palindrome(string_to_check):
    print(f'"{string_to_check}" is a palindrome.')
else:
    print(f'"{string_to_check}" is not a palindrome.')



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Please enter a sentence: ")
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Replace "is" with "was"
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)
