"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
 Given string
string = "Programming"

 Reversing the string using slicing
reversed_string = string[::-1]

 Printing the reversed string
print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
     Split the full name into parts (first name, last name, etc.)
    name_parts = full_name.strip().split()
    
     Extract the first letter of each part, capitalize it, and join with a dot
    initials = '.'.join([part[0].upper() for part in name_parts]) + '.'
    
    return initials

 Get user input for the full name
full_name = input("Enter your full name: ")

 Print the initials in uppercase
print("Initials:", get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
 Input from the user
string = input("Enter a string: ")

 Convert to lowercase to make the check case-insensitive (optional)
string = string.lower()

 Reverse the string using slicing
reversed_string = string[::-1]

 Check if the string is equal to its reverse
if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
     Split the sentence into words using whitespace
    words = sentence.strip().split()
    
     Return the number of words
    return len(words)

 Ask the user to enter a sentence
user_input = input("Enter a sentence: ")

 Count and display the number of words
word_count = count_words(user_input)
print("Number of words:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
 Original string
text = "This is a string and it is an example."

 Replace all occurrences of "is" with "was"
modified_text = text.replace("is", "was")

 Print the modified string
print("Modified string:", modified_text)
