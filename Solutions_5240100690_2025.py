"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Programming"
reversed_string = original_string[::-1]
print("1. Reversed string:", reversed_string)
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("2. Enter your full name: ")
initials = '.'.join([name[0].upper() for name in full_name.split()]) + '.'
print("Initials:", initials)
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
input_string = input("3. Enter a string to check for palindrome: ")
if input_string == input_string[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("4. Enter a sentence: ")
word_count = len(sentence.split())
print("Word count:", word_count)
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
sample_text = "This is a string and it is an example."
modified_text = sample_text.replace("is", "was")
print("5. Modified string:", modified_text)
