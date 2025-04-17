"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
#RESPONSE
string = "Programming"
reversed_string = string[::-1]
print(reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
#RESPONSE
full_name = input("Enter your full name: ").strip()

initials = [name[0].upper() for name in full_name.split()]

formatted_initials = ".".join(initials) + "."

print(formatted_initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#RESPONSE
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1] 

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome!")
else:
    print(f"'{string}' is NOT a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

#RESPONSE
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
#RESPONSE
import re

original_string = "This is a string and it is an example."
modified_string = re.sub(r'\bis\b', 'was', original_string)
print(modified_string)

