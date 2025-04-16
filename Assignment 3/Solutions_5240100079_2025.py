"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
number=float(input("Enter a number:"))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero.")    



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
number= int(input("Enter a number:"))
if number % 2== 0:
    print("number is even.")
else:
    print("The number is odd.")    


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Input string
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for a case-insensitive check
cleaned_text = text.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence:")
words = sentence.split()
print("Number of words:",len(words))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
text = "This is a string and it is an example."

# Replace 'is' with 'was'
# To avoid replacing 'is' inside words like "This", we'll use a regular expression
import re

# Replace 'is' as a whole word
modified_text = re.sub(r'\bis\b', 'was', text)

# Print the result
print(modified_text)
