"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

word = "Programming"
reverse= ""
for pro in word:
    reverse=pro  + reverse
print("Reversed string:", reverse)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

full_name = input("Enter your full name: ")
parts = full_name.strip().split()
initials = ".".join(map(lambda name: name[0].upper(), parts)) + "."
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

text = input("Enter a string to check for palindrome: ")
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break
print("The word is a Palindrome?" , is_palindrome)


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
words = text.split()
for i in range(len(words)):
    if words[i] == "is":
        words[i] = "was"
modified_text = " ".join(words)
print("Modified string:", modified_text)
