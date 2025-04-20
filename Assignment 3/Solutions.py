"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

original_string = "Programming"


reversed_string = original_string[::-1]


print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
original_string = "Programming"


reversed_string = original_string[::-1]


print("Reversed string:", reversed_string)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
user_input = input("Enter a string: ")

cleaned_string = user_input.lower()


if cleaned_string == cleaned_string[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence = input("Enter a sentence: ")


words = sentence.split()


word_count = len(words)


print("Number of words in the sentence:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text = "This is a string and it is an example."


modified_text = text.replace("is", "was")


print("Modified string:", modified_text)
