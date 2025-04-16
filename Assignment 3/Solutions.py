"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text="programming"
reversed text=text[::-1]

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

name parts=full name.strip().split()
initials=".".join([parts[o].upper() 
 for part in name parts])
   print(initials + "."
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text=input("Enter a string: ")
clean text= text.replace(" ","").lower()
if clean text==clean text[::--1]:
   print("it is a pallindrome"
else:
   print("It is not a pallindrome."


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence=input("Enter a sentence: "
word count=len(words)
print("Number of words in the sentence:" word count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text="This is a string and it is an example."
modified text=text.replace("is",  "was")
print(modified text)
