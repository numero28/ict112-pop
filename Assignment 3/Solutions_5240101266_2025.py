"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Solution

s = "Programming"
    reversed_s = s[::-1]
    print("Reversed String:", reversed_s)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Solution

full_name = input("Enter your full name: ")
    names = full_name.split()
    initials = [name[0].upper() for name in names if name]
    print("Initials:", ".".join(initials) + ".")

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Solution

s = input("Enter a string to check for a palindrome: ")
    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Solution

sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Word Count:", len(words))

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Solution

original_string = "This is a string and it is an example."
    modified_string = original_string.replace("is", "was")
    print("Modified String:", modified_string)
