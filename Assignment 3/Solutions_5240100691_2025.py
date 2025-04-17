"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text = "Programming"
reversed_text = text[::-1]
print("Task 1 - Reversed:", reversed_text



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Task 2 - Enter your full name: ")
initials = ''.join([word[0].upper() + '.' for word in full_name.split()])
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
pal_text = input("Task 3 - Enter a string to check if it's a palindrome: ")
if pal_text.lower() == pal_text[::-1].lower():
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Task 4 - Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
replace_text = "This is a string and it is an example."
modified_text = replace_text.replace("is", "was")
print("Task 5 - Modified string:", modified_text)
