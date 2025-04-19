"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
word= "Programming"
reversed_word= word[::-1]
print(reversed_word)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name= input("Enter your full name:  ")
name_part= full_name.split()
initials= ""
for part in name_part:
initials += part[0].upper() + "."
print(initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text= input("Enter a word to check if it's a palindrome: ")
if text== text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence= input("Enter a sentence: ")
words= sentence.split()
for word in words:
    print(word)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re
text= "This is a book and it is an example."
modified_text= re.sub(r"\bis\b", "was", text)
print(modified_text)
