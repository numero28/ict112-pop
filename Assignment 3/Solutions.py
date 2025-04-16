"""
Solutions to assignment 3
"""


"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""language = "programming"
print(language[::-1])
print("\n")


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
username=input("Enter your full name")
username=username.upper()
print(username)
print("/n



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word = input("type your in a palindrome:")
revserse = word[::-1]

if word = word[::-1]
  print(true)
else:
  print(false)


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("type in sentence")
words = sentesnc.split()
number_of_words = len(words)
print(number_of_words)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string = "This is a string and it an example"
print(string.replace("is","was"))
