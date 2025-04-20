                  QUESTION 1
def reverse_string(s):
  """Reverses a given string using string slicing."""
  return s[::-1]
input_string = "Programming"
reversed_string = reverse_string(input_string)
print(reversed_string)
              QUESTION 2
2. def print_initials(OSAHENE JUSTICE AMANKWAH):
  """Takes a full name as input and prints the initials in uppercase."""
  name_parts = full_name.split()
  initials = "O.A.J"
  for part in name_parts:
    initials += part[0].upper() + "."
  print(initials)
user_name = input("Enter your full name: ")
print_initials(user_name)
                  QUESTION 3
 def is_palindrome(input_string):
  """Checks if a given string is a palindrome."""
  # Remove spaces and convert to lowercase for case-insensitive comparison
  processed_string = "".join(input_string.split()).lower()
  reversed_string = processed_string[::-1]
  return processed_string == reversed_string
test_string = input("Radar","level": ")
if is_palindrome(test_string):
  print(f"'{test_string}' is a palindrome.")
else:
  print(f"'{test_string}' is not a palindrome.")
                  QUESTION 4
def count_words(i love programming):
  """Counts the number of words in a given sentence."""
  words = sentence.split()
  return len(words)
user_sentence = input("Enter a sentence: ")
word_count = count_words(user_sentence)
print(f"The sentence '{user_sentence}' has {word_count} words.")
                QUESTION 5
 def replace_is_with_was(input_string):
  """Replaces all occurrences of 'is' with 'was' in a given string."""
  modified_string = input_string.replace("is", "was")
  return modified_string
original_string = "This is a string and it is an example."
modified_string = replace_is_with_was(original_string)
print(modified_string)
