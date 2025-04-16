"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text = "Programming"
for items in reversed(text):
print(items)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [parts[0].upper() for part in name_parts]
result = " . ".join(initials)
print(results)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text = input("Enter a word: ")
text = text.lower()
if text == text[::-1]:
    print("it is a palindrome!")
else:
     print("it is not a palindrom")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"Number of words in the sentence: {word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text = "this is a string and it is an example"
modified_text = text.replace("is", "was")
print(f"Modified string: {modified_text}")
