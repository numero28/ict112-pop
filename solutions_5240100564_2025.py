
"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

# Reverse using slicing
string = "Programming"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

# Taking user input
full_name = input("Enter your full name: ")
# Splitting the name into parts
name_parts = full_name.split()
# Getting the initials
initials = '.'.join([part[0].upper() for part in name_parts]) + '.'
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Check if the string is a palindrome
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Taking user input
sentence = input("Enter a sentence: ")
# Counting words using split()
word_count = len(sentence.split())
print("Number of words:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Given string
text = "This is a string and it is an example."
# Replacing "is" with "was"
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
