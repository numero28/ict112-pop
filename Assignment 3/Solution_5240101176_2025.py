"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.c
Hint: Use string slicing or a loop.
"""
# Reversing a string using slicing
string =  input("Enter the name you want to reverse: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# solution Taking user's full name as input
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]
initials_str = ".".join(initials)
print(f"Initials: {'.'.join(initials)}")



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Checking if a string is a palindrome
string = input("Enter a string to check if it's a palindrome: ")
reversed_string = string[::-1] 
if string == reversed_string:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.") 
  



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Counting the number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Number of words in the sentence: {word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Replacing occurrences of "is" with "was"
string = "This is a string and it is an example."
modified_string = string.replace("is", "was")
print(f"Modified string: {modified_string}")
