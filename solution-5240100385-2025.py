"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string1 = "Programming"
reversed_string1 = string1[::-1]
print(reversed_string1)
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Wusuwe Amos: ")
name_parts = full_name.split()
initials = ""
for part in name_parts:
    initials += part[0].upper() + "."
print(initials[:])
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string2 = input("level: ")
string2 = string2.lower() # Convert to lowercase for case-insensitive comparison
reversed_string2 = string2[::-1]
if string2 == reversed_string2:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Mr. Kingsford is a good man: ")
words = sentence.split()
word_count = len(words)
print("The number of words in the sentence is:", word_count)
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string3 = "This is a string and it is an example."
modified_string3 = string3.replace("is", "was")
print(modified_string3)