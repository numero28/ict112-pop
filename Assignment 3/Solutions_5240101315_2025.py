"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
text = "Programming"

# Reverse the string using slicing
reversed_text = text[::-1]

# Print the result
print("Reversed string:", reversed_text)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")

name_parts = full_name.strip().split()

initials = ""
for part in name_parts:
    initials += part[0].upper() + "."

# Print the result
print("Your initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word = input("Enter a word: ")

# Make both original and reversed lowercase (to ignore case)
word_lower = word.lower()
reversed_word = word_lower[::-1]

# Check if the word is the same as its reverse
if word_lower == reversed_word:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Use split() to break the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
text = "This is a string and it is an example."

# Replace 'is' with 'was'
modified_text = text.replace("is", "was")

# Print the result
print("Modified string:", modified_text)