"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

input_str = "Programming"
reversed_str = reverse_string(input_str)
print("Reversed String:", reversed_str)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def extract_initials(full_name):
    names = full_name.split()
    initials = ".".join(name[0].upper() for name in names)
    return initials + "." if len(names) > 1 else initials

full_name = input("Enter your full name: ")
initials = extract_initials(full_name)
print("Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

word = input("Enter a word to check if it’s a palindrome: ")
if word == word[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
print("This", "is a string and it is an example.".replace("is","was"))



