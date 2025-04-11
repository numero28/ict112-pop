"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
#ANSWER
default_string = "Programming"
reversed_string = defualt_string[::-1]
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
#ANSWER
name = input("Enter your full name: ")
parts = name.split()
initials = [part[0].upper() for part in parts]
print(f"{initials[0]}.{initials[1]}.")


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#ANSWER
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
#ANSWER
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
#ANSWER
sentence = "This is a string and it is an example."
sentence2 = sentence.replace("is", "was")
print(sentence2)