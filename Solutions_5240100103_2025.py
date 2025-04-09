"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

s = "programming"
reversed_s = "" 
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)

""""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
#Get the user's full name and split into parts
name_parts = input().split()

#Extract the first letter of each part,uppercase, and add a dot 
initials = [f"{part[0].upper()}."
for part in name_parts]
#Join and print the result
print("".join(initials))

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#Get input string and remove leading/trailing whitespace
s = input().strip()

#check if the string equalls is reverse
is_palindrome = s == s[::-1]

#Print the result
print("palindrome" if is_palindrome else "Not a palindrome")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
#Get user input and split into words
sentence = input("Enter a sentence:").split()
words = sentence.split()

#Count and display the number of words 
print(f"Number of words:{len(words)}")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

#Original string
original = "This is a string and it is an example."

#split into words, replace "is" with "was", then rejoin
modified = ''.join(['was' if word == 'is'else word for word in original.split()])