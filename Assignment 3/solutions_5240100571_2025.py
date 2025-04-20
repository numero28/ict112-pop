
"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

# 1. Reverse the string "Programming"
string = "Programming"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

# 2. Print initials from full name
full_name = input("Enter your full name: ")
initials = '.'.join([name[0].upper() for name in full_name.split()]) + '.'
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

# 3. Check if a string is a palindrome
text = input("Enter a string to check if it's a palindrome: ")
if text == text[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# 4. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# 5. Replace "is" with "was" in a sentence
original = "This is a string and it is an example."
modified = original.replace("is", "was")
print("Modified string:", modified)

