"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(s):
    """Return the reversed string."""
    return s[::-1]
original_string = "Programming"
reversed_string = reverse_string(original_string)
print("Original String:", original_string)
print("Reversed String:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def extract_initials(full_name):
    names = full_name.split()
    initials = [name[0].upper() for name in names]
    return '.'.join(initials)
full_name = input("Enter your full name: ")
initials = extract_initials(full_name)
if initials:
    print(f"Initials: {initials}.")
else:
    print("Please enter a valid full name.")


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    """Return True if the string is a palindrome, False otherwise."""
    s = s.lower() 
    return s == s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    """Return the number of words in the sentence."""
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"Number of words: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
def replace_string(s):
    """Return the modified string with 'is' replaced by 'was'."""
    return s.replace('is', 'was')
original_string = "This is a string and it is an example."
modified_string = replace_string(original_string)

print("Original String:", original_string)
print("Modified String:", modified_string)