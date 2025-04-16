"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(s):
    return s[::-1]

# Test the function
original_string = "programming"
reversed_string = reverse_string(original_string)

print("Original String:", original_string)
print("Reversed String:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def extract_initials(full_name):
    names = full_name.split()
    initials = ".".join([name[0].upper() for name in names])
    return initials

# Test the function
full_name = input("Enter your full name: ")
initials = extract_initials(full_name)

# Add a dot between initials and at the end
initials_list = list(initials)
for i in range(1, len(initials_list), 2):
    initials_list.insert(i, '.')
initials = ''.join(initials_list) + '.' if len(initials_list) > 1 else initials + '.'

print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]

# Test the function
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
    words = sentence.split()
    return len(words)

# Test the function
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)

print(f"The sentence contains {word_count} words.")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
def replace_string(s):
    return s.replace("is", "was")

# Test the function
original_string = "This is a string and it is an example."
modified_string = replace_string(original_string)

print("Original String:", original_string)
print("Modified String:", modified_string)
