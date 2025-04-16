"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

# Reversing the string using slicing
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

# Function to get initials in uppercase
def get_initials(full_name):
    initials = [name[0].upper() for name in full_name.split()]
    return '.'.join(initials) + '.'

# Example usage
full_name = input("Enter your full name: ")
print(get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Function to count words
def count_words(sentence):
    return len(sentence.split())

# Example usage
sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

# Function to replace 'is' with 'was'
def replace_is_with_was(text):
    return text.replace("is", "was")

# Example usage
sentence = "This is a string and it is an example."
print(replace_is_with_was(sentence))
