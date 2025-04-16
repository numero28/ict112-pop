"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Programming"
reversed_string = ""
for char in original_string:
    reversed_string = char + reversed_string
print("Reversed string (using loop):", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]
initials_str = '.'.join(initials) + '.'
print("Initials:", initials_str)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"Number of words in the sentence: {word_count}"


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."
modified_string = original_string.replace(" is ", " was ")
print("Original string:", original_string)
print("Modified string:", modified_string)  
"""
