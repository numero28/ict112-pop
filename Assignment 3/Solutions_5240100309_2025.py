"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(s):
  return s[::-1]

original_string = "Programming"
reversed_string = reverse_string(original_string)
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def print_initials(full_name):
  name_parts = full_name.split()
  initials = ""
  for part in name_parts:
    initials += part[0].upper() + "."
  print(initials[:-1])
user_name = input("Enter your full name: ")
print_initials(user_name)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(input_string):
  processed_string = "".join(input_string.split()).lower()
  reversed_string = processed_string[::-1]
  return processed_string == reversed_string
text = input("Enter a string: ")
if is_palindrome(text):
  print(f"'{text}' is a palindrome.")
else:
  print(f"'{text}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
  words = sentence.split()
  return len(words)
user_sentence = input("Enter a sentence: ")
word_count = count_words(user_sentence)
print(f"The sentence '{user_sentence}' has {word_count} words.")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)

