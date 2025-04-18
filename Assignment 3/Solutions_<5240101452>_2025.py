"""
Solutions to assignment 3
"""

"""
QUESTION 1
string = "Programming"
reversed_string = string[::-1]
print(reversed_string)


"""
QUESTION 2
def get_initials(full_name):
  name_parts = full_name.split()  
  initials = ""
  for part in name_parts:
    initials += part[0].upper() + "." 
  return initials[:-1] 
full_name = input("Enter your full name: ")
initials = get_initials(full_name)
print(initials)

"""



"""
QUESTION 3
def is_palindrome(input_string):
    processed_string = ''.join(filter(str.isalnum, input_string)).lower()
  return processed_string == processed_string[::-1]
input_string = input("Enter a string: ")
if is_palindrome(input_string):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")

"""



"""
QUESTION 4
def count_words(sentence):
  words = sentence.split()  # Split the sentence into a list of words
  return len(words)  # Return the number of words in the list
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print("The sentence has", word_count, "words.")

"""



"""
QUESTION 5
def replace_is_with_was(input_string):
   return modified_string
original_string = "This is a string and it is an example."
modified_string = replace_is_with_was(original_string)
print(modified_string)

"""
