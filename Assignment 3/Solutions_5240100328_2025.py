"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

# Reversing the string using slicing
original_string = "Programming"
reversed_string = original_string[::-1]

# Printing the reversed string
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

# Taking user input for the full name
full_name = input("Enter your full name: ")

# Splitting the name into words and extracting the initials
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]

# Joining the initials with a dot and printing
initials_string = ".".join(initials) + "."
print(initials_string)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

# Taking user input for the string
input_string = input("Enter a string: ")

# Removing spaces and converting to lowercase for uniform comparison
input_string = input_string.replace(" ", "").lower()

# Checking if the string is equal to its reverse
if input_string == input_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

# Taking user input for the sentence
sentence = input("Enter a sentence: ")

# Splitting the sentence into words using the split() method
words = sentence.split()

# Counting the number of words
word_count = len(words)

# Printing the number of words
print(f"The number of words in the sentence is: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
original_string = "This is a string and it is an example."

# Replacing all occurrences of 'is' with 'was'
modified_string = original_string.replace("is", "was")

# Printing the modified string
print(modified_string)
