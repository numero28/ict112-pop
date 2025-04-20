"```python
# Problem 1 Solution
string_to_reverse = "Programming"
reversed_string = string_to_reverse[::-1]
print("Reversed string:", reversed_string)

# Problem 2 Solution
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() + '.' for part in name_parts]
print("Initials:", ''.join(initials))

# Problem 3 Solution
user_input = input("Enter a string to check for palindrome: ")
if user_input == user_input[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# Problem 4 Solution
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# Problem 5 Solution
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print("Modified string:", modified_string)
```"
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
