"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
item ="programming"
reversed_item = item[::-1]
print("reversed string:",reversed_item)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name=input("enter full name:")
name_parts=full_name.split()
initials=""
for part in name_parts:
    initials += part[0].upper() + "."
    print("Intials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text =input("enter a word: ")
text_lower =text.lower()
if text_lower == text_lower[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("enter sentence: ")
words=sentence.spilt()
word_count=len(words)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
helping_verbs="this is a string and it is an example."
modified_helping_verb=helping_verb.replace("is","was")
print(f"Modified string:{modified_helping_verb}")
