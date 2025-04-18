"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string = "Programme"
reverse = string[::-1]
print(reverse)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
name = input("Enter name: ")
initials = []
for word in name.split():
    initials.append(word[0].upper())
print("Your intials are: ", ".".join(initials) + ".")
    

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
test_string = input("Enter a word: ")
if is_palindrome(test_string):
    print(f"{test_string} is a palindrome!")
else:
    print(f"{test_string} is not a palindrome!")
    


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The number of words in the sentence is :{word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
import re

original_string = "This is a string and it is an example."


modified_string = re.sub(r'\bis\b', 'was', original_string)


print("Modified string:", modified_string)
