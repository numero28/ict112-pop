"""
Solutions to assignment 3
"""
# Question 1

# Reversing using a loop
text = "Programming"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)



# Question 2

# Get the user's full name
full_name = input("Enter your full name: ")

# Split the name into parts (first, last, etc.)
name_parts = full_name.strip().split()

# Get the first letter of each part and convert to uppercase
initials = ""
for part in name_parts:
    initials += part[0].upper() + "."

# Print the initials
print("Initials:", initials)



# Question 3

# Get input from the user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
cleaned_text = text.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



# Question 4

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words using split()
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)



# Question 5

# Original string
text = "This is a string and it is an example."

# Replace "is" with "was"
modified_text = text.replace("is", "was")

# Print the modified string
print("Modified string:", modified_text)
