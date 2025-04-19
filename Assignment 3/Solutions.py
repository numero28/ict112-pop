"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
t = "programming"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

full_name = input("Enter your full name: ")
initials = ".".join(name[0].upper() for name in full_name.split())
print(f"{initials}.")



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome(t):
    t = t.replace(" ", "").lower()
    return t == ""
 t = input("Enter a string: ")
if is_palindrome(t):
    print(f"'{t}' is a palindrome.")
else:
    print(f"'{t}' is not a palindrome.")




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The sentence contains {word_count} words.")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

t = "This is a string and it is an example."
t = t.replace("is", "was")
print(t)
