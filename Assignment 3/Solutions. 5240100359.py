"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Original string
original_string = 'Programming'

# Reversed string using a loop
reversed_string = ''
for char in original_string:
    reversed_string = char + reversed_string

# Print the reversed string
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
f get_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    # Extract the initials and convert them to uppercase
    initials = [part[0].upper() for part in name_parts]
    # Join the initials with a dot
    return '.'.join(initials) + '.'

# Take full name input from the user
user_input = input("Enter your full name: ")
# Get the initials and print them
print(get_initials(user_input))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove any spaces and convert to lowercase
    cleaned_string = s.replace(" ", "").lower()
    # Check if the string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Take user input
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
  


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

Function to count words in a sentence
def count_words(sentence):
    # Use split() to break the sentence into words
    words = sentence.split()
    # Return the number of words
    return len(words)

# Take user input
user_sentence = input("Enter a sentence: ")

# Count the number of words
word_count = count_words(user_sentence)

# Print the result
print(f'Number of words in the sentence: {word_count}')

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Original string
original_string = 'This is a string and it is an example.'

# Replace all occurrences of 'is' with 'was'
modified_string = original_string.replace('is', 'was')

# Print the modified string
print(modified_string)
