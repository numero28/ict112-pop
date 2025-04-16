"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string = "Programming"
reversed_string = string[::-1]
print(reversed_string)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter full name: ")
split_name = full_name.split()
initials = ""

for name in split_name:
    initials += name[0].upper()
    
print(initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string = input("Enter word: ")
reversed_string = string[::-1]
print(reversed_string)

if string.lower() == reversed_string.lower():
    print(f"{string}: Is a Palindrome")
else:
    print("Word is not a Palindrome")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
split_sentence = sentence.split()
number_of_words = len(split_sentence)
print(number_of_words)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string = "This is a string and it is an example."
modified_string = string.replace("is","was")
print(modified_string)