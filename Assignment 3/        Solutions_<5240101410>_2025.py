Question 1:# Original string
original_string = "Programming"

# Reversed string using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

Output:

Reversed string: gnimmargorP





Question 2: # Get full name from the user
full_name = input("Enter your full name: ")


Question 3:

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned = s.replace(" ", "").lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Get user input
input_string = input("Enter a string: ")

# Check and display result
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

Example:

Enter a string: Racecar
The string is a palindrome.

Question 4: 

def count_words(sentence):
    # Split the sentence by spaces and count the resulting words
    words = sentence.split()
    return len(words)

# Get user input
input_sentence = input("Enter a sentence: ")


Question 5:

# Original string
text = "This is a string and it is simple"

# Replace all occurrences of "is" with "was"
# Note: use a word-based replacement to avoid affecting parts of other words
replaced_text = text.replace(" is ", " was ")

print("Original text:", text)
print("Modified text:", replaced_text)

Output:

Original text: This is a string and it is simple
Modified text: This was a string and it was simple




# Count and display the number of words
word_count = count_words(input_sentence)
print(f"The number of words in the sentence is: {word_count}")




# Split the name into words
name_parts = full_name.split()

# Extract the first letter of each word and make it uppercase
initials = ''.join([part[0].upper() for part in name_parts])

# Print the initials
print("Initials:", initials