"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reversing the string using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get user's full name
full_name = input("Enter your full name: ")

# Split the name into parts (e.g., first and last)
name_parts = full_name.strip().split()

# Get the first letter of each part and capitalize it
initials = ".".join([part[0].upper() for part in name_parts]) + "."

# Print the initials
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""# Get input from user
user_string = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = user_string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words using split()
words = sentence.strip().split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""# Original string
original_string = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")

# Print the modified string
print("Modified string:", modified_string)
