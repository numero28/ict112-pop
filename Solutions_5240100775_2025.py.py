"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_str = "Programming"
reversed_str = original_str[::-1]
print(reversed_str)
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get user input and split into name parts
full_name = input("Enter your full name: ").strip().split()

# Extract initials and format them with periods
initials = [name[0].upper() + '.' for name in full_name]

# Join the initials and print the result
print(''.join(initials))

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Compare the string with its reverse
    return s == s[::-1]

# Get input from the user
input_str = input("Enter a string: ")

# Check and print the result
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is NOT a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Get user input
sentence = input("Enter a sentence: ").strip()

# Split into words and count
words = sentence.split()
word_count = len(words)

# Display the result
print(f"Number of words: {word_count}")
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_str = "This is a string and it is an example."

# Split the string into words, replace "is" with "was", then rejoin
modified_str = ' '.join(['was' if word == 'is' else word for word in original_str.split()])

print(modified_str)