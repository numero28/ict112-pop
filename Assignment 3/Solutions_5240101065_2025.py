"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reversing using slicing
reversed_string = original_string[::-1]

# Printing the reversed string
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Taking user input
full_name = input("Enter your full name: ")

# Splitting the name into words
name_parts = full_name.strip().split()

# Extracting initials and converting to uppercase
initials = '.'.join([name[0].upper() for name in name_parts]) + '.'

# Printing the result
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Taking user input
user_string = input("Enter a string: ")

# Making the string lowercase and removing spaces (optional, for flexibility)
cleaned_string = user_string.replace(" ", "").lower()

# Checking if the string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Asking the user to enter a sentence
sentence = input("Enter a sentence: ")

# Splitting the sentence into words using split()
words = sentence.strip().split()

# Counting the number of words
word_count = len(words)

# Displaying the result
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replacing "is" with "was"
modified_string = original_string.replace("is", "was")

# Printing the modified string
print("Modified string:", modified_string)
