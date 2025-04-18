"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

text=”programming”
reversed_text=text[::-1]
print(f”Reversed text is”,{reversed_text})



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
user_name = input(”Enter your name”)
print(user_name.upper() )
print(user_name.upper() [0],”.”,user_name.upper[5]


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

word=input(”enter your word”)
if word==word[::-1]:
  print(f”{word} is a palindrome.”)
else:
  print(f”{word} is not palindrome.”
  
           

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input(”enter your sentence”)
words=sentence.split()
print(words)
print(len(words)
      


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text=”This is a string and it is an example.”
text_new=text.replace(”is”,”was”)
print(text_new)
