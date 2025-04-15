"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
word = "Programming"
reversed_word = word[::-1]
print("Reversed string:", reversed_word)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Type your full name: ")
word_parts = full_name.split()
initials = ""
for i in word_parts:
    initials += i[0].upper() + "."
print(f"Initials: {initials}")



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#Ask the user to enter a word
text = input("Enter a word: ")

text = text.lower()

#reversed the entered word
reversed_text = text[::-1]


if text == reversed_text:
    print(f"The word {text} is a palindrome.")
else:
    print(f"The word {text} is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Use split() to break the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

# Original string
text = "This is a string and it is an example."

# Replace 'is' with 'was'
modified_text = text.replace("is", "was")

# Print the result
print("Modified string:", modified_text)
