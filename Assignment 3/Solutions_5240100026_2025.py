"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text = "programming"
reversed_text = text[::-1]
print(reversed_text)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
fall_name = input("Enter your full name: ")
initials = ''.join([name[0].upper()+'.'for name in full_name.split()])
print(initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text = input("Enter strings: ")
if text == text[::-1]:
  print("pallindrome")
else:
  print("Not a pallindrome")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence:")
words = sentence.split()
PRINT("Number of words :",len(words))

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text = "This is a string and it is a an example."
modified_text = text.replace("is","was")
print(modified_text)
