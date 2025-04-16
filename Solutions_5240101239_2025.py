"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Answer
text = "Programming"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Answer
full_name = input("Enter your full name: ")
name_parts = full_name.strip().split()
initials = [part[0].upper() for part in name_parts]
formatted_initials = ".".join(initials) + "."
print("Initials:", formatted_initials)
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Answer
text = input("Enter a string: ")
cleaned_text = text.replace(" ", "").lower()
reversed_text = cleaned_text[::-1]
if cleaned_text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Answer
sentence = input("Enter a sentence: ")
words = sentence.strip().split()
word_count = len(words)
print("Number of words in the sentence:", word_count)
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Answer
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
