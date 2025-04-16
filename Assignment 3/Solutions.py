"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
revese string="programming"
Reverse reversed_string = original[::-1]
print("1. Reversed string:", reversed_string)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Print initials in uppercase
full_name = input("2. Enter your full name: ").strip()
name_parts = full_name.split()
initials = ".".join([name[0].upper() for name in name_parts]) + "."
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text = input("3. Enter a word to check if it's a palindrome: ").lower()
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("4. Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_text = "This is a string and it is an example."
modified_text = original_text.replace("is", "was")
print("5. Modified string:", modified_text)




