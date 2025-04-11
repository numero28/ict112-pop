"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text="Programming"
text_reverse=[::-1]
print(text_reverse)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def initials(full_name):
  names=full_name.strip().split()
  initials='.'.join([name[0]. upper() for name in names]) +'.'
  return initials 
user_name=input("Enter your full_name: ")
print("Initials:", initials(user_name)
  



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
  s=s.replace("",""). lower()
  reversed_s=''.join(reversed(s))
  return s==reversed_s
string=input("Enter a string: ")
if is_palindrome(string):
  print("Palindrome is a string")
else:
  print("Palindrome is not a string")




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter a sentence: ")
words=sentence.split()
word_count=len(words)
print(word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_sentence="This is a string and it is an example"
new_sentence=original_sentence.replace("is","was")
print(new_sentence)
