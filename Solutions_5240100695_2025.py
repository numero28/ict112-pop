"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string_to_reverse = "Programming"
reversed_string = string_to_reverse[::-1]
print("reversed_string:", reversed_string)
"""

2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
initials = '.'.join(part[0].upper() for part in full_name.split())
print(f"{initials}.")

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#get user input
text = input("enter text: ")

#convert text to lower case
text_lower = text.lower()

#check if the string is equal to its reverse
if text_lower == text_lower[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
word_count = len(sentence.split() )
print(f"Number of words: {word_count}")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text = "This is a string and it is an example."

#replace 'is' with 'was'
modified_text = text.replace("is", "was")

#print the modified string
print("Modified string:", modified_text)