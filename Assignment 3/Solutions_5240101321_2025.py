#QUESTION 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Original string
string_given = "Programming"

# Reversed string using slicing
reversed_text = text[::-1]

# Print the reversed string
print("Reversed string:", reversed_text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#QUESTION 2
""""""""
# Get user's full name
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.strip().split()

# Get the initials and convert to uppercase
initials = ".".join([part[0].upper() for part in name_parts]) + "."

# Print the initials
print("Initials:", initials)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#QUESTION 3
""""""""
# Get input from the user
text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison (optional)
text = text.lower()

# Check if the string is equal to its reverse
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#QUESTION 4
""""""""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words using split()
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#QUESTION 5
""""""""
# Original string
text = "This is a string and it is an example."

# Replace "is" with "was"
modified_text = text.replace("is", "was")

# Print the modified string
print("Modified string:", modified_text)
""""""""
