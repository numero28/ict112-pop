"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original = "programming"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print("Reversed (loop)):",reversed_str)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get user's full name
full_name = input("Enter your full name: ")
# Split the name into parts and get the first letter of each part
initials = [name[0].upper() for name in full_name.split()]
# Join the initials with periods and print
print("Your initials are:", '.'.join(initials) + '.')


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Compare string with its reverse
    return cleaned == cleaned[::-1]
# Test the function
test_string = input("Enter a string to check: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome!")
else:
    print(f"'{test_string}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Get input from user
sentence = input("Please enter a sentence: ")
# Split the sentence into words using split()
words = sentence.split()
# Count the number of words
word_count = len(words)
# Display the result
print(f"Your sentence has {word_count} word(s).")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."
modified_string = original_string.replace(" is ", " was ")
print("Original string:", original_string)
print("Modified string:", modified_string)