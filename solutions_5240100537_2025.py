
"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(s):
  """Reverses a given string.

  Args:
    s: The string to be reversed.

  Returns:
    The reversed string.
  """
  return s[::-1]

# Example usage
original_string = "Programming"
reversed_string = reverse_string(original_string)
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(input_string):
  """Checks if a given string is a palindrome.

  Args:
    input_string: The string to be checked.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Remove spaces and convert to lowercase for case-insensitive comparison
  cleaned_string = "".join(input_string.split()).lower()
  reversed_string = cleaned_string[::-1]
  return cleaned_string == reversed_string

# Get input from the user
test_string = input("Enter a string: ")

# Check if it's a palindrome and print the result
if is_palindrome(test_string):
  print(f"'{test_string}' is a palindrome.")
else:
  print(f"'{test_string}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
  """Counts the number of words in a given sentence.

  Args:
    sentence: The input sentence (string).

  Returns:
    The number of words in the sentence (integer).
  """
  words = sentence.split()
  return len(words)

# Get input from the user
user_sentence = input("Enter a sentence: ")

# Count the words and print the result
word_count = count_words(user_sentence)
print("Number of words:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
def replace_is(input_string):
  """Replaces all occurrences of 'is' with 'was' in a string.

  Args:
    input_string: The string to perform the replacement on.

  Returns:
    The modified string with 'is' replaced by 'was'.
  """
  modified_string = input_string.replace("is", "was")
  return modified_string

# The original string
original_string = "This is a string and it is an example."

# Replace "is" with "was"
modified_string = replace_is(original_string)

# Print the modified string
print("Modified string:", modified_string)
