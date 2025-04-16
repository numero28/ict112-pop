"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

string='Programming'
word=string[::-1]
print(word)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
name=input('Enter Full name here:\n')
name=name.split()
initials=""
for i in name:
    initials+= i[0].upper()+'.'
print(initials.strip('.'))

"""
    3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

word = input('Enter word to check whether it is a palindrome or not. \n')
if word == word[::-1]:
    print('Word is palindrome')
else:
    print('The word is not palindrome')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Please enter sentence to count the number of words\n")
words = sentence.split()
wordCount = 0
for i in words:
    wordCount+=1
print("The number of words in the sentence is",wordCount)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string."
"""
import re
string = "This is a string and it is an example."
newString = re.sub(r'\bis\b','was',string)
print('Old string: This is a string and it is an example.')
print('New string:',newString)



