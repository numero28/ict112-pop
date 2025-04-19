"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Reversing using slicing
original_string = "Programming"
reversed_string = original_string[::-1]  # This slices the string in reverse order
print("Reversed String:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Program to extract initials from full name
def get_initials(full_name):
    words = full_name.split()  # Split name into words
    initials = ".".join([word[0].upper() for word in words])  # Extract and format initials
    return initials + "."  # Adding a final period

# Taking user input
full_name = input("Enter your full name: ")
print("Initials:", get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check if a string is a palindrome
def is_palindrome(string):
    return string.lower() == string.lower()[::-1]  # Convert to lowercase and compare with reversed version

# Taking user input
word = input("Enter a word: ")
if is_palindrome(word):
    print(f'"{word}" is a palindrome!')
else:
    print(f'"{word}" is not a palindrome.')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Prompt the user to enter a sentence
sentence = input("Please enter a sentence: ")

# Use the split() method to break the sentence into words
words = sentence.split()

# Count the number of words in the sentence
word_count = len(words)

# Display the word count
print(f"The number of words in your sentence is: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
# Define the original string
original_string = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")

# Print the modified string
print("Modified string:", modified_string)
"""
