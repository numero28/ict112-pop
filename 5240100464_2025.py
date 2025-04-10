"""
Solutions to assignment 3
"""
5240100464_2025.py
"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original = "Programming"
reversed_str = original[::-1]
print(reversed_str)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
name = input().strip()
parts = name.split()
initials = [part[0].upper() + '.' for part in parts]
print(''.join(initials))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
s = input().strip()
print(s == s[::-1])


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ").strip()
word_count = len(sentence.split())
print(f"Number of words: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original = "This is a string and it is an example."
modified = original.replace("is", "was")
print(modified)
