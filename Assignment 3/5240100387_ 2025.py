Question 1
# Method 1: Using string slicing
text = "Programming"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# Method 2: Using a loop
reversed_text_loop = ""
for char in text:
    reversed_text_loop = char + reversed_text_loop
print("Reversed string (using loop):", reversed_text_loop)

Question 2
# Get user's full name
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.split()

# Get the first letter of each part, make it uppercase, and join with dots
initials = '.'.join([part[0].upper() for part in name_parts]) + '.'

print("Initials:", initials)

Question 3
# Get input from user
text = input("Enter a string: ")

# Convert to lowercase and remove spaces (optional for phrase palindromes)
cleaned_text = text.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

Question 4
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

print("Number of words:", word_count)

Question 5
# Original string
text = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_text = text.replace("is", "was")

print("Modified string:", modified_text)
