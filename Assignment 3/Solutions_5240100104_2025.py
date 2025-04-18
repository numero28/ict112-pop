"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string="Programming"
reveresedString=string[::-1]
print(reveresedString)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
userName=input("Enter your full name here\n: ")
userName=userName.split()
initials=""
for i in userName:
    initials+=i[0].upper()+". "
print(initials.strip())


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word=input("Enter a word to check if it is palindrome or not\n: ")
if word==word[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter a sentence to count the number of words\n: ")
words=sentence.split()  
wordCount=0 
for i in words:
    wordCount+=1
print("The number of words in the sentence is",wordCount)





"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re

string = "This is a string and it is an example."
newString = re.sub(r'\bis\b', 'was', string)
print(newString)
