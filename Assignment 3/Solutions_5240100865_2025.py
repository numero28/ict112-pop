"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Programming"
reversed_string_slicing = original_string[::-1]
print(f"Reversed string (using slicing): {reversed_string_slicing}")


original_string = "Programming"
reversed_string_loop = ""
for char in original_string:
    reversed_string_loop = char + reversed_string_loop
print(f"Reversed string (using loop): {reversed_string_loop}")


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def print_initials(full_name):
  """
  Takes a user's full name as input and prints the initials in uppercase.

  Args:
    full_name: A string representing the user's full name.
  """
  name_parts = full_name.split()
  initials = ""
  for part in name_parts:
    if part:  
      initials += part[0].upper() + "."
  print(initials)

user_name = input("Enter your full name: ")

print_initials(user_name)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(input_string):
  """
  Checks if a given string is a palindrome.

  Args:
    input_string: The string to be checked.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  processed_string = ''.join(filter(str.isalnum, input_string)).lower()
  reversed_string = processed_string[::-1]
  return processed_string == reversed_string

test_string = input("Enter a string: ")

if is_palindrome(test_string):
  print(f"'{test_string}' is a palindrome.")
else:
  print(f"'{test_string}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
  """
  Counts the number of words in a given sentence.

  Args:
    sentence: A string representing the sentence.

  Returns:
    An integer representing the number of words in the sentence.
  """
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
