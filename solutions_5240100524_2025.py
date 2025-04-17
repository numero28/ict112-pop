"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "programming"
reversed_string = original_string[::-1]
print("original string:",original_string)
print("reversed string:",reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name =input("Enter your full name: ")
names = full_name.split()
initials = ".".join(name[0].upper() for name in names)
if initials:
    initials += "."
print("Your initials are: ",initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = input("enter a string: ")
if is_palindrome(string):
    print(f" '{string} ' is a palindrome.")
else:
    print(f" '{string} ' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("enter a sentence: ")
words = sentence.split()
print("Number of words: ",len(words))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = ("This is a string and it is an example.")
modified_string = original_string.replace("is" ,  " was")
print("modified string: ",modified_string)
