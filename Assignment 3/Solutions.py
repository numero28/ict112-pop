"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
#  Reverse the string "Programming"
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

#  Print the initials in uppercase from a full name
full_name = input("Enter your full name: ")
name_parts = full_name.strip().split()
initials = ".".join([part[0].upper() for part in name_parts]) + "."
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#  Check if a given string is a palindrome
text = input("Enter a string to check for palindrome: ")
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
#  Count number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.strip().split()
word_count = len(words)
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Replace all occurrences of "is" with "was"
original_sentence = "This is a string and it is an example."
modified_sentence = original_sentence.replace("is", "was")
print("Modified sentence:", modified_sentence)
