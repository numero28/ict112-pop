"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

Here's a Python program to reverse the string "Programming" using string slicing:


string = "Programming"
reversed_string = string[::-1]
print(reversed_string)


Output: gnimmargorP

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

Here's a Python program that takes a user's full name as input and prints the initials in uppercase:


def print_initials(full_name):
    # Split the full name into individual names
    names = full_name.split()

    # Extract the initials and convert to uppercase
    initials = ".".join([name[0].upper() for name in names])

    # Add a dot after each initial
    formatted_initials = ".".join(initials)

    # Print the formatted initials
    print(f"{formatted_initials}.")

# Get the user's full name
full_name = input("Enter your full name: ")

# Call the function to print the initials
print_initials(full_name)


Here's a more concise version:


full_name = input("Enter your full name: ")
initials = ".".join(name[0].upper() for name in full_name.split())
print(f"{initials}.")


Example usage:


Enter your full name: john doe
J.D.
Histins Asare Kyeremeh

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Here's a Python program to check if a given string is a palindrome:


def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")


Example usage:


Enter a string: radar
'radar' is a palindrome.

Enter a string: hello
'hello' is not a palindrome.


This program works by comparing the input string with its reverse (s[::-1]). If they're the same, the string is a palindrome. It also removes spaces and converts to lowercase to ensure the comparison is case-insensitive.


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Here's a Python program that asks the user to enter a sentence and counts the number of words in the sentence:


def count_words(sentence):
     Remove leading and trailing whitespace
    sentence = sentence.strip()

     Split the sentence into words
    words = sentence.split()

     Return the number of words
    return len(words)

 Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

 Count and print the number of words
word_count = count_words(sentence)
print(f"The sentence contains {word_count} words.")


Example usage:


Enter a sentence: Hello world, this is a test.
The sentence contains 6 words.


This program works by:

1. Removing leading and trailing whitespace from the input sentence.
2. Splitting the sentence into words using the split() method, which splits on whitespace by default.
3. Returning the number of words using the len() function.

You can also write a more concise version:


sentence = input("Enter a sentence: ")
print(f"The sentence contains {len(sentence.split())} words.")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

Here's a Python program to replace all occurrences of "is" with "was" in the given string:


# Define the string
string = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_string = string.replace("is", "was")

# Print the modified string
print(modified_string)


Output:

This was a string and it was an example.


This program uses the replace() method, which replaces all occurrences of the specified substring ("is") with the replacement string ("was").

Note that this replacement is case-sensitive. If you want a case-insensitive replacement, you can use the re.sub() function from the re module:


import re

string = "This is a string and it is an example."
modified_string = re.sub("is", "was", string, flags=re.IGNORECASE)
print(modified_string)
