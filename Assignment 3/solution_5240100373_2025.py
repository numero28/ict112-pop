# Original string
original_string = "Programming"

# Reversed string using slicing
reversed_string = original_string[::-1]

# Print the result
print("Reversed string:", reversed_string)



#exercise 2
# Get user's full name
full_name = input("Enter your full name: ")

# Split the name into words
name_parts = full_name.strip().split()

# Extract initials and convert to uppercase
initials = ".".join([name[0].upper() for name in name_parts]) + "."

# Print the initials
print("Initials:", initials)



#exercise 3
# Get input from the user
text = input("Enter a string: ")

# Convert to lowercase and remove spaces (optional, for more flexibility)
processed_text = text.replace(" ", "").lower()

# Check if the string is equal to its reverse
if processed_text == processed_text[::-1]:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')



#exercise 4
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)



#exercise 5
# Original string
text = "This is a string and it is an example."

# Replace "is" with "was"
modified_text = text.replace("is", "was")

# Print the result
print("Modified string:", modified_text)
