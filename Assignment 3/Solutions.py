"""
solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Question 1: Reverse the string "Programming"
text = "Programming"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Question 2: Get user’s initials in uppercase from their full name
full_name = input("Enter your full name: ")
names = full_name.strip().split()  # splits the full name into separate words
initials = ".".join([name[0].upper() for name in names]) + "."
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Question 3: Check if the given word is a palindrome
word = input("Enter a word: ")
if word.lower() == word[::-1].lower():
    print("It's a palindrome.")
else:
    print("Not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Question 4: Count the number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Question 5: Replace "is" with "was" in the given text
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified text:", modified_text)
