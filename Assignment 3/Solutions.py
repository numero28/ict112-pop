"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Original string
text = "Programming"
Reverse the string using slicing
reversed_text = text[::-1]
 Print the reversed string
print("Reversed string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    # Split the full name into parts (first name, last name, etc.)
    name_parts = full_name.strip().split()
    
    # Extract the first letter of each part, capitalize it, and join with a dot
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
def is_palindrome(text):
Remove spaces and convert to lowercase for a fair comparison
    cleaned = text.replace(" ", "").lower()
   Check if the string is equal to its reverse
    return cleaned == cleaned[::-1]
 Get user input
user_input = input("Enter a string: ")
Check and display result
if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    Split the sentence into words using the split() method
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
Replace all occurrences of 'is' with 'was'
modified_text = text.replace(" is ", " was ")
Also replace 'is' if it is at the beginning or end of the string
modified_text = modified_text.replace(" is.", " was.").replace(" is ", " was ")
Print the modified string
print("Modified string:", modified_text)
