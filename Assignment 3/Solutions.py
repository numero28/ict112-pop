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
def get_initials(name):
    initials = '.'.join([part[0].upper() for part in name.split()])
    return initials

full_name = input("Enter your full name: ")
print("Initials:", get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(string):
    return string == string[::-1]

user_string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome.')
else:
    print(f'"{user_string}" is not a palindrome.')



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    words = sentence.split()
    return len(words)

user_sentence = input("Enter a sentence: ")
print("Number of words:", count_words(user_sentence))



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."

modified_string = original_string.replace("is", "was")

print("Modified string:", modified_string)
