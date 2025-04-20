"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Reversing the string "Programming"
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Print initials from full name
full_name = input("Enter your full name: ")
initials = '.'.join([name[0].upper() for name in full_name.strip().split()]) + '.'
print("Your Initials=", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# 3. Check if a string is a palindrome
text = input("Enter a string to check if it's a palindrome: ")
if text == text[::-1]:
    print("{text} is a palindrome")
else:
    print("{text} not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Count the number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Replace "is" with "was" in a string
original_sentence = "This is a string and it is an example."
modified_sentence = original_sentence.replace("is", "was")
print("Modified sentence:", modified_sentence)