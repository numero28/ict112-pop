"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""# Original string
original_string = "Programming"

# Reversing the string using slicing
reversed_string = original_string[::-1]

# Printing the reversed string
print(reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Function to get the initials from the full name
def get_initials(full_name):
    # Split the full name into words
    name_parts = full_name.split()
    
    # Extract initials and convert to uppercase
    initials = [part[0].upper() for part in name_parts]
    
    # Join initials with periods
    return '.'.join(initials) + '.'

# Taking input from the user
user_full_name = input("Enter your full name: ")

# Getting and printing the initials
initials = get_initials(user_full_name)
print(initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned_string = s.replace(" ", "").lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Taking input from the user
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""# Function to count the number of words in a sentence
def count_words(sentence):
    # Split the sentence into words based on spaces
    words = sentence.split()
    return len(words)

# Taking input from the user
user_sentence = input("Enter a sentence: ")

# Counting the number of words
word_count = count_words(user_sentence)

# Displaying the result
print(f'The number of words in the sentence is: {word_count}')



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")

# Print the modified string
print("Modified string:", modified_string)
