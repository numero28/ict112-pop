"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
word = 'Programming'
opp = word[::-1]
print(opp)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
fullname = input('Enter your fullname: ')
part = fullname.strip().split()
sj = ""
for e in part:
    sj += e[0].upper() + '.'
print(sj)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
palindrome = input('Enter word to check: ')
if palindrome == palindrome[::-1]:
    print(True)
else:
    print(False)

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sen = input('Enter the sentence: ')
parts = sen.split()
total = len(parts)
print(total)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re


text = "This is a string and it is an example."


modified_text = re.sub(r'\bis\b', 'was', text)
print(modified_text)

