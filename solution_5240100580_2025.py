
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
def get_initials(full_name):
  """Extracts and returns the uppercase initials of a full name.

  Args:
    full_name: The full name as a string.

  Returns:
    A string containing the uppercase initials separated by periods.
  """
  names = full_name.split()
  initials = ""
  for name in names:
    initials += name[0].upper() + "."
  return initials.rstrip(".") # Remove the trailing period

# Get input from the user
user_name = input("Enter your full name: ")

# Get and print the initials
name_initials = get_initials(user_name)
print(name_initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(text):
  """Checks if a given string is a palindrome (reads the same forwards and backward).

  Args:
    text: The string to be checked.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  processed_text = ''.join(filter(str.isalnum, text)).lower()
  return processed_text == processed_text[::-1]

# Get input from the user
input_string = input("Enter a string: ")

# Check if it's a palindrome and print the result
if is_palindrome(input_string):
  print(f"'{input_string}' is a palindrome.")
else:
  print(f"'{input_string}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
  """Counts the number of words in a given sentence.

  Args:
    sentence: The input sentence as a string.

  Returns:
    The number of words in the sentence.
  """
  words = sentence.split()
  return len(words)

# Get input from the user
user_sentence = input("Enter a sentence: ")

# Count the words and print the result
word_count = count_words(user_sentence)
print(f"The sentence has {word_count} words.")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)
