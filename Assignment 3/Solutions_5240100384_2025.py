"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# For loop 
mainWord = "Programming"

theReversedWord = ""

for letters in mainWord: 
    theReversedWord = letters + theReversedWord 

print(theReversedWord)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    name_parts = full_name.strip().split()

    initials = [part[0].upper() for part in name_parts if part]
    return '.'.join(initials)

full_name = input("Enter your full name: ")
print("Initials:", get_initials(full_name)) 



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""