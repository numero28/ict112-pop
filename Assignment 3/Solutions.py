"""
Solutions_5240101151_2025.py
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string = "programming"
reversed_string = string[::-1]
print(f"Reversed_string{reversed_string:}")

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
name = input("Enter your name:")
initials ="".join([word[0].upper()for word in name.spilt()])
print(f"Your initials are: {initials}")

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text = input("Enter a string: ")
if text == text[::-1]:
  print("The string is a palindrome.")
else:
  print("The string is not palindrome.")
  
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
words = sentences.split()
word_count = len(words)
print(f"The number of words in the seentence is: {word_count}")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text =("This is a string and it is an example.")
modified_text = text.replace("is","was")
print(f"modified string:{modified_text}")
