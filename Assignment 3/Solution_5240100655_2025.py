"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string1 = "Programming"
reversed_string1 = string1[::-1]
print(f"The reversed string of '{string1}' is: {reversed_string1}")

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = ""
for part in name_parts:
    initials += part[0].upper() + "."
print(f"The initials of '{full_name}' are: {initials}")

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string2 = input("Enter a string to check if it's a palindrome: ")
string2 = string2.lower()  # Ignore case
reversed_string2 = string2[::-1]
if string2 == reversed_string2:
    print(f"'{string2}' is a palindrome.")
else:
    print(f"'{string2}' is not a palindrome.")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The sentence '{sentence}' has {word_count} words.")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string3 = "This is a string and it is an example."
modified_string3 = string3.replace("is", "was")
print(f"The modified string is: {modified_string3}")