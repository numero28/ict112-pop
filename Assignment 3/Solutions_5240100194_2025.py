"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
#Solution
name = "Programming"
reversed_name = name [::-1]
print("Reversed name:", reversed_name )

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
#Solution
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]
uppercase_initials = '.'.join(initials)+ '.'
print("Initials:", uppercase_initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#Solution
word = input("Enter any word: ")
word_lowercase = word.lower()
word_reverse = word_lowercase[::-1]
if word_lowercase == word_reverse:
    print("Yes, it is palindrome")
else:
    print("No, it's not palindrome")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
#Solution
sentence = input("Enter your sentence: ")
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence provided: ",word_count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
#Solution
import re
text = "This is a string and it is an example"
modified_text = re.sub(r"\bis\b", "was", text)
print("Modified string:", modified_text)
