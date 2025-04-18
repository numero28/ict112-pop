"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string="Programming"
reversed_string=string[::-1]
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name=input("Enter your name\n")
initials=".".join([name[0].upper() for name in full_name.split()])+"."
print(initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string=input("Enter a string\n")
if string==string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter your sentence\n")
words=sentence.split()
print("Number of words:",len(words))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re


original_string="This is a string and this is a test. Is this another test?"
modified_string=re.sub(r'\bis\b','was', original_string.replace ,"was")
print("Original string",original_string)
print("Modified string:",modified_string)
