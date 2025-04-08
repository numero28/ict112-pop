"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
 Define the string
text = "Programming"

 Reverse the string using slicing
reversed_text = text[::-1]

 Print the reversed string
print(reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")

 Split the full name into first and last names
name_parts = full_name.split()

 Extract the initials and convert them to uppercase
initials = "".join([part[0].upper() for part in name_parts])

 Print the initials in the desired format
print(".".join(initials) + ".")



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string = input("Enter a string: ")

 Check if the string is the same as its reverse
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
 Get the sentence from the user
sentence = input("Enter a sentence: ")

 Split the sentence into words using split() and count the number of words
words = sentence.split()

 Print the number of words
print("Number of words in the sentence:", len(words))

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
 Replace 'is' with 'was'
modified_text = text.replace(" is ", " was ")

 Print the modified string
print(modified_text)
