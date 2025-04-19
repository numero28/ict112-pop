"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Program to reverse the string "Programming"
string = "Programming"
reversed_string = string[::-1]  # Using string slicing
print(reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""# Program to get initials from the user's full name
full_name = input("Enter your full name: ")
initials = ''.join([name[0].upper() + '.' for name in full_name.split()])
print(initials)




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""# Program to check if a given string is a palindrome
string = input("Enter a string: ")
if string == string[::-1]:  # Comparing the string with its reverse
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""# Program to count the number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())  # Using split() method to break the string into words
print(f'Number of words: {word_count}')




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""# Program to replace "is" with "was" in a specific string
original_string = "This is a string and it is an example."
modified_string = original_string.replace(" is ", " was ")  # Replacing occurrences
print(modified_string)
