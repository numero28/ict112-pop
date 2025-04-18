"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
python
text = "Programming"
reversed_text = text[::-1]  # Slice with step -1
print(reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(name):
    # Split the name into words
    words = name.split()
    
    # Extract the first letter of each word and convert to uppercase
    initials = ".".join([word[0].upper() for word in words])
    
    return initials

# Get user input
full_name = input("Enter your full name: ")

# Print the initials
print(get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Convert to lowercase to make the check case-insensitive
    s = s.lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Get user input
text = input("Enter a string: ")

# Check if it's a palindrome and print the result
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    # Split the sentence into words using spaces as separators
    words = sentence.split()
    
    # Return the number of words
    return len(words)

# Get user input
sentence = input("Enter a sentence: ")

# Print the word count
print("Number of words:", count_words(sentence))

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_text = text.replace("is", "was")

# Print the modified string
print(modified_text)