"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def print_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    
    # Extract the first letter of each part and join them with '.'
    initials = '.'.join(part[0].upper() for part in name_parts)
    
    # Add a '.' at the end if there are initials
    if len(name_parts) > 1:
        initials += '.'
    
    print(initials)

# Get user input
full_name = input("Enter your full name: ")

# Print the initials
print_initials(full_name)





"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Get user input
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Return the number of words
    return len(words)

# Get user input
sentence = input("Enter a sentence: ")

# Count the number of words
word_count = count_words(sentence)

# Print the result
print(f"The sentence contains {word_count} words.")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)
