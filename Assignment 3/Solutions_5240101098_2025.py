"""Solutions to assignment 3"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop. 
"""
original_string = "Programming"

# Using a loop
reversed_string = ""
for i in original_string:
    reversed_string = i + reversed_string
print("Reversed string (using loop):", reversed_string)

"""
 2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D." 
"""
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = ""
for i in name_parts:
    initials += i[0].upper() + "."
print("Initials:", initials[:-1])

""" 
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse. 
"""


def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    processed_string = "".join(input_string.split()).lower()
    reversed_string = processed_string[::-1]
    return processed_string == reversed_string


# Get input from the user
test_string = input("Enter a string to check if it's a palindrome: ")

# Check if it's a palindrome and print the result
if is_palindrome(test_string):
    print(test_string, "is a palindrome.")
else:
    print(test_string, "is not a palindrome.")

""" 
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words. 
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
number_of_words = len(words)
print("The sentence has", number_of_words, "words.")

""" 
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string. 
"""
sentence = "This is how i grew"
modified_sentence = sentence.replace("is", "was")
print("Modified string:", modified_sentence)
