#QUESTION 1
# Original string
original_string = "Programming"
# Reversing the string using a loop
reversed_string = ""
for char in original_string:
    reversed_string = char + reversed_string
# Printing the reversed string
print(reversed_string)


#QUESTION 2
# Function to get initials from a full name
def get_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    # Extract the first letter of each part and convert to uppercase
    initials = [part[0].upper() for part in name_parts]
    # Join the initials with a dot and return
    return '.'.join(initials) + '.'

# Taking user input
user_fullname = input("Enter your full name: ")

# Getting the initials
initials = get_initials(user_fullname)

# Printing the initials
print(initials)

#QUESTION 3
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Taking user input
user_string = input("Enter a string: ")

# Checking if the string is a palindrome
if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome.')
else:
    print(f'"{user_string}" is not a palindrome.')

#QUESTION 4
# Function to count the number of words in a sentence
def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Return the number of words
    return len(words)

# Taking user input
user_sentence = input("Enter a sentence: ")

# Counting the number of words
word_count = count_words(user_sentence)

# Printing the result
print(f'The number of words in the sentence is: {word_count}')

#QUESTION 5

# Original string
original_string = "This is a string and it is an example."

# Replacing all occurrences of "is" with "was"
modified_string = original_string.replace("is", "was")

# Printing the modified string
print(modified_string)

